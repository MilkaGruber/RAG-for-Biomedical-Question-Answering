"""Create reproducible manual-review artifacts from RAG.py JSON results."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


CATEGORIES = [
    "irrelevant retrieval",
    "relevant but insufficient retrieval",
    "misleading or contradictory context",
    "context supports wrong option",
    "model ignored useful context",
    "too much context / context dilution",
    "prompt or output parsing failure",
    "ambiguous question / questionable gold label",
    "other",
]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Export baseline-correct/RAG-wrong cases for manual analysis."
    )
    parser.add_argument("--results", default="rag_results.json")
    parser.add_argument("--run", type=int, default=-1,
                        help="Run index; -1 means the latest run.")
    parser.add_argument("--k", type=int,
                        help="k to inspect; omitted when the run has only one k.")
    parser.add_argument("--output", default="rag_corruption_review")
    parser.add_argument("--summarize", action="store_true",
                        help="Summarize the manually annotated output CSV.")
    return parser.parse_args()


def load_run(path, run_index):
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    runs = data if isinstance(data, list) else [data]
    try:
        return runs[run_index]
    except IndexError as error:
        raise ValueError(
            f"Run {run_index} does not exist; the file contains {len(runs)} run(s)."
        ) from error


def resolve_k(run, requested_k):
    available = list(run.get("rag_by_k", {}))
    if requested_k is not None:
        if str(requested_k) not in available:
            raise ValueError(f"k={requested_k} is not in: {', '.join(available)}")
        return requested_k
    if len(available) != 1:
        raise ValueError("Select one k with --k. Available: " + ", ".join(available))
    return int(available[0])


def corrupted_cases(run, k):
    cases = []
    for detail in run.get("evaluation_details", []):
        baseline = detail.get("baseline", {})
        rag = detail.get("rag_by_k", {}).get(str(k))
        gold = detail.get("expected")
        if rag and baseline.get("prediction") == gold and rag.get("prediction") != gold:
            cases.append(detail)
    return cases


def option_text(case, letter):
    if letter is None:
        return "(no valid answer)"
    return case.get("options", {}).get(letter, "(unavailable)")


def write_csv(path, cases, k):
    fields = [
        "question_id", "k", "subject", "topic", "question", "gold_letter",
        "gold_option", "rag_letter", "rag_option", "failure_category",
        "retrieval_contains_answer", "misleading_document_rank", "notes",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for case in cases:
            rag_letter = case["rag_by_k"][str(k)].get("prediction")
            writer.writerow({
                "question_id": case.get("question_id"), "k": k,
                "subject": case.get("subject_name"), "topic": case.get("topic_name"),
                "question": case.get("question"), "gold_letter": case.get("expected"),
                "gold_option": option_text(case, case.get("expected")),
                "rag_letter": rag_letter, "rag_option": option_text(case, rag_letter),
                "failure_category": "", "retrieval_contains_answer": "",
                "misleading_document_rank": "", "notes": "",
            })


def markdown_cell(value):
    if value is None:
        return "N/A"
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_markdown(path, run, cases, k, results_path, run_index):
    config = run.get("config", {})
    lines = [
        "# RAG corruption review", "",
        f"- Source results: `{results_path}`",
        f"- Requested run index: `{run_index}`",
        f"- Run time: {run.get('run_time', 'unknown')}",
        f"- Experiment size: {run.get('questions', 'unknown')} questions",
        f"- RAG setting: k={k}",
        f"- Question-only retrieval: `{config.get('question_only', 'unknown')}`",
        f"- Corrupted answers: {len(cases)}", "",
        "## Run configuration", "",
        "| Parameter | Value |", "|---|---|",
    ]
    lines.extend(
        f"| {markdown_cell(parameter)} | {markdown_cell(value)} |"
        for parameter, value in config.items()
    )
    lines.extend([
        "",
        "## Coding guide", "", "Choose one primary category in the CSV:", "",
    ])
    lines.extend(f"- {category}" for category in CATEGORIES)
    lines.extend([
        "", "First decide whether the needed fact occurs in the retrieved passages. "
        "Then decide whether retrieval or answer generation caused the failure.", "",
    ])
    for number, case in enumerate(cases, 1):
        rag = case["rag_by_k"][str(k)]
        gold, rag_letter = case.get("expected"), rag.get("prediction")
        lines.extend([
            f"## {number}. Question {case.get('question_id', 'unknown')}", "",
            f"**Subject/topic:** {case.get('subject_name') or 'unknown'} / "
            f"{case.get('topic_name') or 'unknown'}", "",
            case.get("question", "Question text unavailable."), "",
        ])
        lines.extend(f"- {letter}. {text}" for letter, text in case.get("options", {}).items())
        lines.extend([
            "", f"**Gold and baseline:** {gold}. {option_text(case, gold)}  ",
            f"**RAG answer:** {rag_letter}. {option_text(case, rag_letter)}  ",
            f"**Raw baseline output:** `{case.get('baseline', {}).get('raw_answer')}`  ",
            f"**Raw RAG output:** `{rag.get('raw_answer')}`", "",
            "### Retrieved passages", "",
        ])
        for document in case.get("retrieved_documents", [])[:k]:
            lines.extend([
                f"#### Rank {document.get('rank')}: {document.get('title', 'untitled')} "
                f"(similarity {document.get('similarity', 0):.4f})", "",
                document.get("content", "Passage content unavailable."), "",
            ])
        if case.get("dataset_explanation"):
            lines.extend(["**Dataset explanation:** " + case["dataset_explanation"], ""])
        lines.extend(["---", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def summarize(csv_path, output_path):
    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))
    annotated = [row for row in rows if row.get("failure_category", "").strip()]
    counts = Counter(row["failure_category"].strip() for row in annotated)
    lines = [
        "# Manual failure-analysis summary", "",
        f"- Corrupted cases: {len(rows)}", f"- Annotated cases: {len(annotated)}",
        f"- Unannotated cases: {len(rows) - len(annotated)}", "",
        "| Category | Count | Share of annotated cases |", "|---|---:|---:|",
    ]
    for category, count in counts.most_common():
        share = count / len(annotated) if annotated else 0
        lines.append(f"| {category} | {count} | {share:.1%} |")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Summary written to {output_path}")


def main():
    args = parse_arguments()
    stem = Path(args.output)
    csv_path = stem.with_suffix(".csv")
    if args.summarize:
        summary_path = stem.with_name(stem.name + "_summary").with_suffix(".md")
        summarize(csv_path, summary_path)
        return
    results_path = Path(args.results)
    run = load_run(results_path, args.run)
    k = resolve_k(run, args.k)
    cases = corrupted_cases(run, k)
    markdown_path = stem.with_suffix(".md")
    write_csv(csv_path, cases, k)
    write_markdown(markdown_path, run, cases, k, results_path, args.run)
    expected = run["rag_by_k"][str(k)].get("broke_answers")
    print(f"Extracted {len(cases)} corrupted answers for k={k}.")
    if expected is not None and expected != len(cases):
        print(f"Warning: aggregate results report {expected} corrupted answers.")
    print(f"Annotation CSV: {csv_path}")
    print(f"Readable review: {markdown_path}")


if __name__ == "__main__":
    main()
