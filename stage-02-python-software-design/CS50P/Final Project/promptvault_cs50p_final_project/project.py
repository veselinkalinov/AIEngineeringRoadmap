"""PromptVault: an offline prompt library and quality analyzer.

This module contains the command-line application and all core business logic for CS50P final project. The application uses only Python's standard library at runtime and stores its data in a local JSON file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence

DEFAULT_DATA_FILE = Path("prompt_library.json")
MAX_PROMPT_LENGTH = 20_000
QUALITY_DIMENSIONS = (
    "has_role",
    "has_context",
    "has_task",
    "has_constraints",
    "has_output_format",
    "has_examples",
    "has_success_criteria",
)


def main(argv: Sequence[str] | None = None) -> int:
    """Run PromptVault's command-line interface and return an exit status."""

    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    try:
        return args.handler(args)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


def normalize_prompt(text: str) -> str:
    """Normalize line endings and excess blank lines without changing meaning."""

    if not isinstance(text, str):
        raise TypeError("Prompt text must be a string.")

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+$", "", line) for line in normalized.split("\n")]
    normalized = "\n".join(lines).strip()
    return re.sub(r"\n{3,}", "\n\n", normalized)


def analyze_prompt(text: str) -> dict[str, Any]:
    """Analyze a prompt and return measurable quality indicators and a score."""

    normalized = normalize_prompt(text)
    words = re.findall(r"\b[\w'-]+\b", normalized, flags=re.UNICODE)
    sentences = [
        sentence.strip()
        for sentence in re.split(r"[.!?]+(?:\s+|$)", normalized)
        if sentence.strip()
    ]
    lowered = normalized.casefold()

    analysis: dict[str, Any] = {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "average_sentence_length": round(len(words) / len(sentences), 1)
        if sentences
        else 0.0,
        "has_role": _matches(
            lowered,
            r"\b(act as|you are|assume the role|role\s*:|serve as)\b",
        ),
        "has_context": _matches(
            lowered,
            r"\b(context|background|given that|based on|source material|information below|audience)\b",
        ),
        "has_task": _matches(
            lowered,
            r"\b(task|create|write|analy[sz]e|implement|build|explain|compare|summari[sz]e|generate|design|review|calculate|identify)\b",
        ),
        "has_constraints": _matches(
            lowered,
            r"\b(must|must not|do not|never|only|requirements?|constraints?|avoid|limit|without)\b",
        ),
        "has_output_format": _matches(
            lowered,
            r"\b(output|format|return|respond|provide|json|markdown|table|bullet|section|schema)\b",
        ),
        "has_examples": _matches(
            lowered,
            r"\b(example|examples|for example|sample)\b|\be\.g\.",
        ),
        "has_success_criteria": _matches(
            lowered,
            r"\b(success|criteria|ensure|verify|validate|accurate|complete|correct|check)\b",
        ),
        "has_delimiters": bool(
            "```" in normalized
            or '"""' in normalized
            or "'''" in normalized
            or re.search(r"<[^>]+>.*?</[^>]+>", normalized, flags=re.DOTALL)
        ),
    }
    analysis["score"] = calculate_score(analysis)
    return analysis


def calculate_score(analysis: dict[str, Any]) -> int:
    """Calculate a quality score from zero to one hundred."""

    weights = {
        "has_role": 10,
        "has_context": 15,
        "has_task": 20,
        "has_constraints": 15,
        "has_output_format": 15,
        "has_examples": 10,
        "has_success_criteria": 10,
    }

    missing = [key for key in (*weights, "word_count") if key not in analysis]
    if missing:
        raise ValueError(f"Analysis is missing required field(s): {', '.join(missing)}")

    score = sum(weight for key, weight in weights.items() if analysis[key])
    word_count = analysis["word_count"]

    if not isinstance(word_count, int) or word_count < 0:
        raise ValueError("word_count must be a non-negative integer.")

    if 25 <= word_count <= 500:
        score += 5
    elif 10 <= word_count <= 800:
        score += 3
    elif word_count > 0:
        score += 1

    return min(score, 100)


def generate_suggestions(analysis: dict[str, Any]) -> list[str]:
    """Return actionable suggestions for the missing prompt-quality dimensions."""

    suggestions: list[str] = []
    suggestion_map = {
        "has_role": "State the role or perspective the assistant should adopt.",
        "has_context": "Add relevant background, audience, or source context.",
        "has_task": "State one explicit action or goal using a clear task verb.",
        "has_constraints": "Add boundaries such as must, must not, limits, or exclusions.",
        "has_output_format": "Specify the required response format or structure.",
        "has_examples": "Include a short example when the expected result may be ambiguous.",
        "has_success_criteria": "Define how correctness, completeness, or quality should be checked.",
    }

    for dimension, suggestion in suggestion_map.items():
        if not analysis.get(dimension, False):
            suggestions.append(suggestion)

    word_count = analysis.get("word_count", 0)
    if word_count < 10:
        suggestions.append("Add enough detail for the task to be unambiguous.")
    elif word_count > 800:
        suggestions.append(
            "Remove repeated or low-value context to make the prompt easier to follow."
        )

    if analysis.get("average_sentence_length", 0) > 30:
        suggestions.append(
            "Split long sentences into shorter instructions or separate sections."
        )

    if not suggestions:
        suggestions.append(
            "All quality dimensions are present. Refine wording based on real test outputs."
        )

    return suggestions


def build_prompt_template(
    role: str,
    goal: str,
    context: str,
    constraints: Sequence[str],
    output_format: str,
) -> str:
    """Build a reusable structured prompt from user-supplied components."""

    role = normalize_prompt(role)
    goal = normalize_prompt(goal)
    context = normalize_prompt(context)
    output_format = normalize_prompt(output_format)
    cleaned_constraints = [
        normalize_prompt(constraint)
        for constraint in constraints
        if normalize_prompt(constraint)
    ]

    if not goal:
        raise ValueError("A goal is required to build a prompt template.")
    if not output_format:
        raise ValueError("An output format is required to build a prompt template.")

    sections: list[str] = []
    if role:
        sections.extend(("## Role", role, ""))

    sections.extend(("## Goal", goal, ""))

    if context:
        sections.extend(("## Context", context, ""))

    if cleaned_constraints:
        sections.append("## Constraints")
        sections.extend(f"- {constraint}" for constraint in cleaned_constraints)
        sections.append("")

    sections.extend(
        (
            "## Output Format",
            output_format,
            "",
            "## Success Criteria",
            "Ensure the response is accurate, complete, internally consistent, and follows every constraint above.",
        )
    )
    return "\n".join(sections)


def create_prompt_record(
    title: str,
    category: str,
    text: str,
    *,
    record_id: str | None = None,
    created_at: str | None = None,
) -> dict[str, Any]:
    """Create and validate a serializable prompt record."""

    title = normalize_prompt(title)
    category = normalize_prompt(category).casefold() or "general"
    text = normalize_prompt(text)

    if not title:
        raise ValueError("Title cannot be empty.")
    if not text:
        raise ValueError("Prompt text cannot be empty.")
    if len(text) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Prompt text cannot exceed {MAX_PROMPT_LENGTH:,} characters.")

    timestamp = created_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    _parse_timestamp(timestamp, "created_at")
    if record_id is not None and (
        not isinstance(record_id, str) or not record_id.strip()
    ):
        raise ValueError("record_id must be a non-empty string.")
    score = analyze_prompt(text)["score"]
    return {
        "id": record_id or uuid.uuid4().hex[:12],
        "title": title,
        "category": category,
        "text": text,
        "created_at": timestamp,
        "updated_at": timestamp,
        "score": score,
    }


def update_prompt_record(
    record: dict[str, Any],
    *,
    title: str | None = None,
    category: str | None = None,
    text: str | None = None,
    updated_at: str | None = None,
) -> dict[str, Any]:
    """Return an updated copy of a prompt record while preserving its identity."""

    _validate_record(record, "existing")
    if title is None and category is None and text is None:
        raise ValueError("At least one change is required.")

    next_title = record["title"] if title is None else normalize_prompt(title)
    next_category = (
        record["category"]
        if category is None
        else normalize_prompt(category).casefold() or "general"
    )
    next_text = record["text"] if text is None else normalize_prompt(text)

    if not next_title:
        raise ValueError("Title cannot be empty.")
    if not next_text:
        raise ValueError("Prompt text cannot be empty.")
    if len(next_text) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Prompt text cannot exceed {MAX_PROMPT_LENGTH:,} characters.")

    timestamp = updated_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    _parse_timestamp(timestamp, "updated_at")
    if _parse_timestamp(timestamp, "updated_at") < _parse_timestamp(
        record["created_at"], "created_at"
    ):
        raise ValueError("updated_at cannot be earlier than created_at.")

    updated = {
        **record,
        "title": next_title,
        "category": next_category,
        "text": next_text,
        "updated_at": timestamp,
        "score": analyze_prompt(next_text)["score"],
    }
    _validate_record(updated, "updated")
    return updated


def search_records(
    records: Sequence[dict[str, Any]],
    *,
    query: str | None = None,
    category: str | None = None,
    sort_by: str = "created",
    descending: bool = True,
) -> list[dict[str, Any]]:
    """Filter and sort prompt records without modifying the input sequence."""

    sort_keys = {
        "created": lambda record: record["created_at"],
        "updated": lambda record: record["updated_at"],
        "title": lambda record: record["title"].casefold(),
        "category": lambda record: record["category"].casefold(),
        "score": lambda record: record["score"],
    }
    if sort_by not in sort_keys:
        choices = ", ".join(sort_keys)
        raise ValueError(f"Unsupported sort field '{sort_by}'. Choose from: {choices}.")

    wanted_category = normalize_prompt(category).casefold() if category else None
    wanted_query = normalize_prompt(query).casefold() if query else None
    filtered: list[dict[str, Any]] = []
    for record in records:
        _validate_record(record, "search")
        if wanted_category and record["category"].casefold() != wanted_category:
            continue
        searchable = "\n".join(
            (record["id"], record["title"], record["category"], record["text"])
        ).casefold()
        if wanted_query and wanted_query not in searchable:
            continue
        filtered.append(record)

    return sorted(filtered, key=sort_keys[sort_by], reverse=descending)


def _parse_timestamp(value: str, field: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{field} timestamp must be a string.")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{field} timestamp is invalid.") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field} timestamp must include a timezone offset.")
    return parsed


def _validate_record(record: dict[str, Any], label: str | int) -> None:
    required_fields = {
        "id",
        "title",
        "category",
        "text",
        "created_at",
        "updated_at",
        "score",
    }
    if not isinstance(record, dict) or not required_fields.issubset(record):
        raise ValueError(f"Prompt record {label} is incomplete or invalid.")

    for field in ("id", "title", "category", "text"):
        value = record[field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Prompt record {label} has an invalid {field} field.")
    if len(record["text"]) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Prompt record {label} text exceeds the maximum length.")

    created = _parse_timestamp(record["created_at"], "created_at")
    updated = _parse_timestamp(record["updated_at"], "updated_at")
    if updated < created:
        raise ValueError(f"Prompt record {label} has an invalid timestamp order.")

    score = record["score"]
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
        raise ValueError(f"Prompt record {label} has an invalid score field.")


def load_library(path: Path | str) -> list[dict[str, Any]]:
    """Load a prompt library from JSON, returning an empty library if absent."""

    library_path = Path(path)
    if not library_path.exists():
        return []

    try:
        data = json.loads(library_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("The prompt library contains invalid JSON.") from error

    if not isinstance(data, list):
        raise ValueError("The prompt library must contain a JSON list.")

    required_fields = {"id", "title", "category", "text", "created_at"}
    seen_ids: set[str] = set()
    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict) or not required_fields.issubset(record):
            raise ValueError(f"Prompt record {index} is incomplete or invalid.")
        _validate_record(record, index)
        if record["id"] in seen_ids:
            raise ValueError(f"Prompt library contains duplicate ID '{record['id']}'.")
        seen_ids.add(record["id"])

    return data


def save_library(path: Path | str, records: Sequence[dict[str, Any]]) -> None:
    """Save records atomically as readable UTF-8 JSON."""

    seen_ids: set[str] = set()
    for index, record in enumerate(records, start=1):
        _validate_record(record, index)
        if record["id"] in seen_ids:
            raise ValueError(f"Prompt library contains duplicate ID '{record['id']}'.")
        seen_ids.add(record["id"])

    library_path = Path(path)
    library_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = library_path.with_suffix(library_path.suffix + ".tmp")
    serialized = json.dumps(list(records), indent=2, ensure_ascii=False)
    temporary_path.write_text(serialized + "\n", encoding="utf-8")
    os.replace(temporary_path, library_path)


def compare_prompts(first_text: str, second_text: str) -> dict[str, Any]:
    """Compare two prompts and report their score and dimensional differences."""

    first = analyze_prompt(first_text)
    second = analyze_prompt(second_text)
    changed_dimensions = {
        dimension: {
            "first": first[dimension],
            "second": second[dimension],
        }
        for dimension in QUALITY_DIMENSIONS
        if first[dimension] != second[dimension]
    }

    difference = second["score"] - first["score"]
    if difference > 0:
        winner = "second"
    elif difference < 0:
        winner = "first"
    else:
        winner = "tie"

    return {
        "first_score": first["score"],
        "second_score": second["score"],
        "difference": difference,
        "winner": winner,
        "changed_dimensions": changed_dimensions,
    }


def summarize_library(records: Sequence[dict[str, Any]]) -> dict[str, Any]:
    """Calculate aggregate statistics for a sequence of prompt records."""

    if not records:
        return {
            "count": 0,
            "average_score": 0.0,
            "highest_scoring": None,
            "categories": {},
        }

    highest = max(records, key=lambda record: record["score"])
    categories = Counter(record["category"] for record in records)
    average = sum(record["score"] for record in records) / len(records)

    return {
        "count": len(records),
        "average_score": round(average, 1),
        "highest_scoring": {
            "id": highest["id"],
            "title": highest["title"],
            "score": highest["score"],
        },
        "categories": dict(sorted(categories.items())),
    }


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for all PromptVault commands."""

    parser = argparse.ArgumentParser(
        description="Store, analyze, compare, and export prompts without sending them online."
    )
    parser.add_argument(
        "--data-file",
        type=Path,
        default=DEFAULT_DATA_FILE,
        help="JSON library path (default: prompt_library.json)",
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a prompt to the library")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--category", default="general")
    _add_prompt_source_arguments(add_parser, required=False)
    add_parser.set_defaults(handler=_command_add)

    list_parser = subparsers.add_parser("list", help="List saved prompts")
    list_parser.add_argument("--category")
    list_parser.add_argument(
        "--query", help="Search IDs, titles, categories, and prompt text"
    )
    list_parser.add_argument(
        "--sort",
        choices=("created", "updated", "title", "category", "score"),
        default="created",
        dest="sort_by",
    )
    list_parser.add_argument(
        "--ascending",
        action="store_true",
        help="Sort from lowest/oldest to highest/newest",
    )
    list_parser.set_defaults(handler=_command_list)

    show_parser = subparsers.add_parser("show", help="Show a complete saved prompt")
    show_parser.add_argument("id")
    show_parser.set_defaults(handler=_command_show)

    edit_parser = subparsers.add_parser("edit", help="Edit a saved prompt")
    edit_parser.add_argument("id")
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--category")
    _add_prompt_source_arguments(edit_parser, required=False)
    edit_parser.set_defaults(handler=_command_edit)

    analyze_parser = subparsers.add_parser("analyze", help="Analyze a prompt")
    _add_target_arguments(analyze_parser)
    analyze_parser.set_defaults(handler=_command_analyze)

    suggest_parser = subparsers.add_parser(
        "suggest", help="Show improvements for a prompt"
    )
    _add_target_arguments(suggest_parser)
    suggest_parser.set_defaults(handler=_command_suggest)

    compare_parser = subparsers.add_parser("compare", help="Compare two saved prompts")
    compare_parser.add_argument("first_id")
    compare_parser.add_argument("second_id")
    compare_parser.set_defaults(handler=_command_compare)

    stats_parser = subparsers.add_parser("stats", help="Show library statistics")
    stats_parser.set_defaults(handler=_command_stats)

    export_parser = subparsers.add_parser(
        "export", help="Export a saved prompt analysis to Markdown"
    )
    export_parser.add_argument("id")
    export_parser.add_argument("--output", type=Path, required=True)
    export_parser.set_defaults(handler=_command_export)

    delete_parser = subparsers.add_parser("delete", help="Delete a saved prompt")
    delete_parser.add_argument("id")
    delete_parser.add_argument(
        "--yes", action="store_true", help="Delete without asking for confirmation"
    )
    delete_parser.set_defaults(handler=_command_delete)

    template_parser = subparsers.add_parser(
        "template", help="Generate a structured prompt template"
    )
    template_parser.add_argument("--role", default="")
    template_parser.add_argument("--goal", required=True)
    template_parser.add_argument("--context", default="")
    template_parser.add_argument(
        "--constraint", action="append", default=[], dest="constraints"
    )
    template_parser.add_argument("--output", required=True, dest="output_format")
    template_parser.add_argument(
        "--save-title", help="Also save the generated template under this title"
    )
    template_parser.add_argument("--category", default="template")
    template_parser.set_defaults(handler=_command_template)

    return parser


def _matches(text: str, pattern: str) -> bool:
    return bool(re.search(pattern, text, flags=re.IGNORECASE))


def _add_prompt_source_arguments(
    parser: argparse.ArgumentParser, *, required: bool
) -> None:
    group = parser.add_mutually_exclusive_group(required=required)
    group.add_argument("--prompt", help="Prompt text supplied directly")
    group.add_argument("--file", type=Path, help="Read prompt text from a UTF-8 file")


def _add_target_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", help="ID of a saved prompt")
    group.add_argument("--prompt", help="Prompt text supplied directly")
    group.add_argument("--file", type=Path, help="Read prompt text from a UTF-8 file")


def _read_multiline_prompt() -> str:
    print("Paste the prompt. Enter a line containing only END when finished:")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def _read_text_file(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"Prompt file does not exist: {path}")
    return path.read_text(encoding="utf-8")


def _find_record(records: Sequence[dict[str, Any]], record_id: str) -> dict[str, Any]:
    for record in records:
        if record["id"] == record_id:
            return record
    raise ValueError(f"No prompt found with ID '{record_id}'.")


def _resolve_target(args: argparse.Namespace) -> tuple[str, str]:
    if getattr(args, "id", None):
        record = _find_record(load_library(args.data_file), args.id)
        return record["title"], record["text"]
    if getattr(args, "prompt", None) is not None:
        return "Unsaved prompt", args.prompt
    if getattr(args, "file", None) is not None:
        return args.file.name, _read_text_file(args.file)
    raise ValueError("No prompt source was supplied.")


def _command_add(args: argparse.Namespace) -> int:
    if args.prompt is not None:
        text = args.prompt
    elif args.file is not None:
        text = _read_text_file(args.file)
    else:
        text = _read_multiline_prompt()

    record = create_prompt_record(args.title, args.category, text)
    records = load_library(args.data_file)
    if any(existing["id"] == record["id"] for existing in records):
        raise ValueError("Generated a duplicate prompt ID. Please try again.")
    records.append(record)
    save_library(args.data_file, records)
    print(
        f"Saved '{record['title']}' with ID {record['id']} and score {record['score']}/100."
    )
    return 0


def _command_list(args: argparse.Namespace) -> int:
    records = search_records(
        load_library(args.data_file),
        query=args.query,
        category=args.category,
        sort_by=args.sort_by,
        descending=not args.ascending,
    )
    return _print_record_table(records)


def _print_record_table(records: Sequence[dict[str, Any]]) -> int:
    if not records:
        print("No prompts found.")
        return 0
    header = f"{'ID':<12}  {'Score':>5}  {'Category':<15}  Title"
    print(header)
    print("-" * len(header))
    for record in records:
        print(
            f"{record['id']:<12}  {record['score']:>5}  {record['category']:<15.15}  {record['title']}"
        )
    return 0


def _command_show(args: argparse.Namespace) -> int:
    record = _find_record(load_library(args.data_file), args.id)
    print(f"Title: {record['title']}")
    print(f"ID: {record['id']}")
    print(f"Category: {record['category']}")
    print(f"Created: {record['created_at']}")
    print(f"Updated: {record['updated_at']}")
    print(f"Score: {record['score']}/100")
    print("Prompt: ")
    print(record["text"])
    return 0


def _command_edit(args: argparse.Namespace) -> int:
    records = load_library(args.data_file)
    record = _find_record(records, args.id)
    if args.prompt is not None:
        text = args.prompt
    elif args.file is not None:
        text = _read_text_file(args.file)
    else:
        text = None

    updated = update_prompt_record(
        record,
        title=args.title,
        category=args.category,
        text=text,
    )
    updated_records = [updated if item["id"] == args.id else item for item in records]
    save_library(args.data_file, updated_records)
    print(
        f"Updated '{updated['title']}' (ID {updated['id']}) with score {updated['score']}/100."
    )
    return 0


def _command_analyze(args: argparse.Namespace) -> int:
    title, text = _resolve_target(args)
    analysis = analyze_prompt(text)
    _print_analysis(title, analysis)
    return 0


def _command_suggest(args: argparse.Namespace) -> int:
    title, text = _resolve_target(args)
    analysis = analyze_prompt(text)
    print(f"Suggestions for {title} ({analysis['score']}/100):")
    for index, suggestion in enumerate(generate_suggestions(analysis), start=1):
        print(f"{index}. {suggestion}")
    return 0


def _command_compare(args: argparse.Namespace) -> int:
    records = load_library(args.data_file)
    first = _find_record(records, args.first_id)
    second = _find_record(records, args.second_id)
    result = compare_prompts(first["text"], second["text"])

    print(f"First:  {first['title']}: {result['first_score']}/100")
    print(f"Second: {second['title']}: {result['second_score']}/100")
    if result["winner"] == "tie":
        print("Result: the prompts have equal scores.")
    else:
        winner = first if result["winner"] == "first" else second
        print(
            f"Result: '{winner['title']}' scores higher by {abs(result['difference'])} point(s)."
        )

    if result["changed_dimensions"]:
        print("Changed quality dimensions:")
        for dimension, values in result["changed_dimensions"].items():
            label = dimension.removeprefix("has_").replace("_", " ").title()
            print(f"- {label}: {values['first']} -> {values['second']}")
    else:
        print("The measured quality dimensions are identical.")
    return 0


def _command_stats(args: argparse.Namespace) -> int:
    stats = summarize_library(load_library(args.data_file))
    print(f"Saved prompts: {stats['count']}")
    print(f"Average score: {stats['average_score']}/100")
    if stats["highest_scoring"]:
        best = stats["highest_scoring"]
        print(f"Highest score: {best['title']} ({best['score']}/100, ID {best['id']})")
    print("Categories:")
    if not stats["categories"]:
        print("- None")
    else:
        for category, count in stats["categories"].items():
            print(f"- {category}: {count}")
    return 0


def _command_export(args: argparse.Namespace) -> int:
    records = load_library(args.data_file)
    record = _find_record(records, args.id)
    analysis = analyze_prompt(record["text"])
    suggestions = generate_suggestions(analysis)

    rows = []
    for dimension in QUALITY_DIMENSIONS:
        label = dimension.removeprefix("has_").replace("_", " ").title()
        rows.append(f"| {label} | {'Yes' if analysis[dimension] else 'No'} |")

    prompt_as_quote = "\n".join(
        f"> {line}" if line else ">" for line in record["text"].splitlines()
    )
    report = "\n".join(
        (
            f"# Prompt Analysis: {record['title']}",
            "",
            f"- **ID:** `{record['id']}`",
            f"- **Category:** {record['category']}",
            f"- **Created:** {record['created_at']}",
            f"- **Quality score:** {analysis['score']}/100",
            f"- **Word count:** {analysis['word_count']}",
            f"- **Average sentence length:** {analysis['average_sentence_length']} words",
            "",
            "## Quality Dimensions",
            "",
            "| Dimension | Present |",
            "|---|---|",
            *rows,
            "",
            "## Suggested Improvements",
            "",
            *(
                f"{index}. {suggestion}"
                for index, suggestion in enumerate(suggestions, start=1)
            ),
            "",
            "## Original Prompt",
            "",
            prompt_as_quote,
            "",
        )
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Exported report to {args.output}.")
    return 0


def _command_delete(args: argparse.Namespace) -> int:
    records = load_library(args.data_file)
    record = _find_record(records, args.id)

    if not args.yes:
        answer = input(f"Delete '{record['title']}'? [y/N] ").strip().casefold()
        if answer not in {"y", "yes"}:
            print("Deletion cancelled.")
            return 0

    remaining = [item for item in records if item["id"] != args.id]
    save_library(args.data_file, remaining)
    print(f"Deleted '{record['title']}'.")
    return 0


def _command_template(args: argparse.Namespace) -> int:
    prompt = build_prompt_template(
        args.role,
        args.goal,
        args.context,
        args.constraints,
        args.output_format,
    )
    print(prompt)

    if args.save_title:
        record = create_prompt_record(args.save_title, args.category, prompt)
        records = load_library(args.data_file)
        records.append(record)
        save_library(args.data_file, records)
        print(
            f"\nSaved template as '{record['title']}' with ID {record['id']} and score {record['score']}/100."
        )
    return 0


def _print_analysis(title: str, analysis: dict[str, Any]) -> None:
    print(f"Analysis: {title}")
    print(f"Score: {analysis['score']}/100")
    print(f"Words: {analysis['word_count']}")
    print(f"Sentences: {analysis['sentence_count']}")
    print(f"Average sentence length: {analysis['average_sentence_length']} words")
    print("Quality dimensions:")
    for dimension in QUALITY_DIMENSIONS:
        label = dimension.removeprefix("has_").replace("_", " ").title()
        mark = "yes" if analysis[dimension] else "no"
        print(f"- {label}: {mark}")
    print(f"- Delimiters: {'yes' if analysis['has_delimiters'] else 'no'}")


if __name__ == "__main__":
    raise SystemExit(main())
