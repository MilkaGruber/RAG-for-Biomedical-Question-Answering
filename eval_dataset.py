"""Validate the assumptions made when evaluating on MedMCQA."""

from collections import Counter
from numbers import Integral

from datasets import load_dataset


DATASET_NAME = "openlifescienceai/medmcqa"
SPLIT_NAME = "validation"
SINGLE_CHOICE_TYPES = {"single", "single choice", "single-choice"}
MAX_EXAMPLES_TO_PRINT = 10


def normalized_choice_type(value):
    """Normalize harmless spelling/capitalization differences."""
    if not isinstance(value, str):
        return None
    return " ".join(value.strip().lower().split())


def is_single_answer_label(value):
    """A usable MedMCQA label must be one scalar option index from 0 to 3."""
    return isinstance(value, Integral) and not isinstance(value, bool) and 0 <= value <= 3


def validate_single_choice(split):
    required_fields = {
        "id", "question", "opa", "opb", "opc", "opd", "cop", "choice_type"
    }
    missing_fields = required_fields - set(split.column_names)
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Dataset is missing required fields: {missing}")

    choice_type_counts = Counter(str(value) for value in split["choice_type"])
    label_counts = Counter(str(value) for value in split["cop"])
    non_single_choice_rows = []
    invalid_label_rows = []

    for row_number, example in enumerate(split):
        choice_type = normalized_choice_type(example["choice_type"])
        choice_type_is_single = choice_type in SINGLE_CHOICE_TYPES
        label_is_single = is_single_answer_label(example["cop"])

        if not choice_type_is_single:
            non_single_choice_rows.append(
                {
                    "row": row_number,
                    "id": example["id"],
                    "choice_type": example["choice_type"],
                    "cop": example["cop"],
                    "question": example["question"],
                }
            )
        if not label_is_single:
            invalid_label_rows.append(
                {
                    "row": row_number,
                    "id": example["id"],
                    "cop": example["cop"],
                    "question": example["question"],
                }
            )

    print(f"Dataset: {DATASET_NAME}")
    print(f"Split: {SPLIT_NAME}")
    print(f"Questions checked: {len(split)}")
    print(f"choice_type counts: {dict(choice_type_counts)}")
    print(f"cop counts: {dict(label_counts)}")
    print("\nCorrect-answer label representation:")
    print(f"  Exactly one scalar cop value in 0-3: {len(split) - len(invalid_label_rows)}")
    print(f"  Missing, non-scalar, or out-of-range cop: {len(invalid_label_rows)}")

    if invalid_label_rows:
        print(
            f"\nLABEL ERROR: found {len(invalid_label_rows)} question(s) without "
            "exactly one usable cop label."
        )
        for example in invalid_label_rows[:MAX_EXAMPLES_TO_PRINT]:
            print(
                f"  row={example['row']}, id={example['id']!r}, "
                f"cop={example['cop']!r}"
            )
            print(f"    question: {example['question']}")

    if non_single_choice_rows:
        print(
            f"\nCHOICE-TYPE WARNING: {len(non_single_choice_rows)} question(s) are "
            "flagged as 'multi', even though each still has one scalar cop label."
        )
        print(
            "The cop field cannot represent any additional correct options, so this "
            "dataset alone cannot tell us which other answers (if any) are accepted."
        )
        print(
            f"Showing the first {min(len(non_single_choice_rows), MAX_EXAMPLES_TO_PRINT)}:"
        )
        for example in non_single_choice_rows[:MAX_EXAMPLES_TO_PRINT]:
            print(
                f"  row={example['row']}, id={example['id']!r}, "
                f"choice_type={example['choice_type']!r}, cop={example['cop']!r}"
            )
            print(f"    question: {example['question']}")

    all_declared_single_choice = not non_single_choice_rows
    all_labels_valid = not invalid_label_rows
    if all_declared_single_choice and all_labels_valid:
        print("\nPASSED: all questions are declared single-choice and have one valid label.")
    else:
        print("\nFAILED: the validation split is not entirely declared single-choice.")

    return all_declared_single_choice and all_labels_valid


def main():
    validation_split = load_dataset(DATASET_NAME, split=SPLIT_NAME)
    if not validate_single_choice(validation_split):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
