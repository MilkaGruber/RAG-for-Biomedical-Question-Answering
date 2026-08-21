"""Count review labels in all four question-only RAG analysis CSV files."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


ANALYSIS_DIR = Path(__file__).resolve().parent / "analysis_of_500_questions"
DEFAULT_FILES = (
    ANALYSIS_DIR / "rag_corruption_review_fixed_QO_false.csv",
    ANALYSIS_DIR / "rag_corruption_review_QO_false.csv",
    ANALYSIS_DIR / "rag_corruption_review_fixed_QO_true.csv",
    ANALYSIS_DIR / "rag_corruption_review_QO_true.csv",
)

# Schema name -> columns whose values should be counted.
SCHEMAS = {
    "successful RAG answers": ("success_category", "supporting_document_rank"),
    "failed RAG answers": ("failure_category", "retrieval_contains_answer"),
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    """Return the header and data rows from ``path``."""
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError(f"CSV file has no header: {path}")
        return reader.fieldnames, list(reader)


def detect_schema(fieldnames: Iterable[str]) -> tuple[str, tuple[str, ...]]:
    """Identify the review schema from its column names."""
    available = set(fieldnames)
    for schema_name, columns in SCHEMAS.items():
        if set(columns) <= available:
            return schema_name, columns

    expected = " or ".join(" + ".join(columns) for columns in SCHEMAS.values())
    raise ValueError(f"Unrecognized CSV schema; expected {expected}.")


def count_column(rows: Iterable[dict[str, str]], column: str) -> Counter[str]:
    """Count non-empty values, splitting semicolon-separated rank citations."""
    counts: Counter[str] = Counter()
    for row in rows:
        value = (row.get(column) or "").strip()
        if not value:
            continue

        values = re.split(r"[;,]", value) if column == "supporting_document_rank" else [value]
        counts.update(item.strip() for item in values if item.strip())
    return counts


def sort_key(item: tuple[str, int]) -> tuple[int, int, int | str]:
    """Sort by count, with numeric labels before nonnumeric labels on ties."""
    label, count = item
    if label.isdigit():
        return -count, 0, int(label)
    return -count, 1, label.casefold()


def qo_setting(path: Path) -> str:
    """Return the QO setting encoded in a review filename."""
    name = path.stem.lower()
    if name.endswith("_qo_true"):
        return "true"
    if name.endswith("_qo_false"):
        return "false"
    return "not specified"


def analyze(path: Path) -> None:
    """Read one CSV and print counts for its detected schema."""
    fieldnames, rows = read_csv(path)
    schema_name, columns = detect_schema(fieldnames)

    print("-" * 72)
    print(f"File:        {path.name}")
    print(f"QO setting:  {qo_setting(path)}")
    print(f"Result type: {schema_name}")
    print(f"Total rows:  {len(rows)}")

    for column in columns:
        title = column.replace("_", " ").capitalize()
        print(f"\n{title}:")
        counts = count_column(rows, column)
        if not counts:
            print("  (no values)")
            continue
        for value, count in sorted(counts.items(), key=sort_key):
            print(f"  {value:<45} {count:>4}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count categories and retrieval fields in RAG review CSVs."
    )
    parser.add_argument(
        "csv_files",
        nargs="*",
        type=Path,
        default=DEFAULT_FILES,
        help="CSV files to analyze (defaults to all four QO review files).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        print("RAG CORRUPTION REVIEW COUNTS")
        print("=" * 72)
        for path in args.csv_files:
            analyze(path)
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
