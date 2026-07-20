"""Tests for PromptVault's public functions."""

import json
import re

import pytest
from project import (
    analyze_prompt,
    build_prompt_template,
    calculate_score,
    compare_prompts,
    create_prompt_record,
    generate_suggestions,
    load_library,
    main,
    normalize_prompt,
    save_library,
    search_records,
    summarize_library,
    update_prompt_record,
)


def test_normalize_prompt():
    raw = "  First line   \r\n\r\n\r\nSecond line\t  \r\n"
    assert normalize_prompt(raw) == "First line\n\nSecond line"
    assert normalize_prompt("    indented code\n") == "indented code"


def test_normalize_prompt_rejects_non_string():
    with pytest.raises(TypeError):
        normalize_prompt(123)  # type: ignore[arg-type]


def test_analyze_prompt():
    prompt = """
    Act as a Python reviewer.
    Context: the audience is a beginner.
    Task: review the code below and identify bugs.
    You must not rewrite unrelated code.
    Return a Markdown table.
    Example columns: issue, reason, fix.
    Ensure every claim is correct and verified.
    """
    result = analyze_prompt(prompt)

    assert result["score"] == 100
    assert result["has_role"] is True
    assert result["has_context"] is True
    assert result["has_task"] is True
    assert result["has_constraints"] is True
    assert result["has_output_format"] is True
    assert result["has_examples"] is True
    assert result["has_success_criteria"] is True
    assert result["word_count"] >= 25


def test_analyze_prompt_handles_empty_text():
    result = analyze_prompt("")
    assert result["score"] == 0
    assert result["word_count"] == 0
    assert result["sentence_count"] == 0


def test_calculate_score():
    complete_analysis = {
        "has_role": True,
        "has_context": True,
        "has_task": True,
        "has_constraints": True,
        "has_output_format": True,
        "has_examples": True,
        "has_success_criteria": True,
        "word_count": 100,
    }
    assert calculate_score(complete_analysis) == 100

    minimal_analysis = {
        "has_role": False,
        "has_context": False,
        "has_task": True,
        "has_constraints": False,
        "has_output_format": False,
        "has_examples": False,
        "has_success_criteria": False,
        "word_count": 3,
    }
    assert calculate_score(minimal_analysis) == 21


def test_calculate_score_rejects_incomplete_analysis():
    with pytest.raises(ValueError, match="missing required field"):
        calculate_score({"word_count": 20})


def test_generate_suggestions():
    analysis = analyze_prompt("Write a poem.")
    suggestions = generate_suggestions(analysis)

    assert any("role" in suggestion.casefold() for suggestion in suggestions)
    assert any("format" in suggestion.casefold() for suggestion in suggestions)
    assert any("detail" in suggestion.casefold() for suggestion in suggestions)


def test_build_prompt_template():
    result = build_prompt_template(
        "Act as a tutor.",
        "Explain recursion.",
        "The learner knows basic Python.",
        ["Use one code example.", "Do not use advanced mathematics."],
        "Return three short sections in Markdown.",
    )

    assert "## Role" in result
    assert "## Goal" in result
    assert "## Context" in result
    assert "- Use one code example." in result
    assert "## Output Format" in result
    assert "## Success Criteria" in result


def test_build_prompt_template_requires_goal_and_output():
    with pytest.raises(ValueError, match="goal"):
        build_prompt_template("", "", "", [], "Markdown")
    with pytest.raises(ValueError, match="output format"):
        build_prompt_template("", "Explain Python", "", [], "")


def test_library_round_trip(tmp_path):
    path = tmp_path / "nested" / "library.json"
    record = create_prompt_record(
        "Test Prompt",
        "Coding",
        "Act as a reviewer. Analyze this code and return a table. Ensure correctness.",
        record_id="abc123",
        created_at="2026-07-18T12:00:00+00:00",
    )

    save_library(path, [record])
    loaded = load_library(path)

    assert loaded == [record]
    assert json.loads(path.read_text(encoding="utf-8"))[0]["id"] == "abc123"


def test_load_library_missing_file_returns_empty_list(tmp_path):
    assert load_library(tmp_path / "missing.json") == []


def test_load_library_rejects_invalid_json(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid JSON"):
        load_library(path)


def test_compare_prompts():
    first = "Write a summary."
    second = (
        "Act as an editor. Context: the reader is a student. "
        "Summarize the text. You must use only five bullets. "
        "Return Markdown. Example: one fact per bullet. Ensure accuracy and completeness."
    )

    comparison = compare_prompts(first, second)

    assert comparison["winner"] == "second"
    assert comparison["difference"] > 0
    assert comparison["second_score"] > comparison["first_score"]
    assert "has_role" in comparison["changed_dimensions"]


def test_summarize_library():
    records = [
        create_prompt_record(
            "Short",
            "writing",
            "Write a poem.",
            record_id="one",
            created_at="2026-07-18T12:00:00+00:00",
        ),
        create_prompt_record(
            "Detailed",
            "coding",
            (
                "Act as a Python reviewer. Context: this is beginner code. "
                "Analyze the program and identify bugs. You must preserve comments. "
                "Return a Markdown table. Example columns: issue and fix. "
                "Ensure every finding is correct and complete."
            ),
            record_id="two",
            created_at="2026-07-18T12:01:00+00:00",
        ),
    ]

    summary = summarize_library(records)

    assert summary["count"] == 2
    assert summary["average_score"] > 0
    assert summary["highest_scoring"]["id"] == "two"
    assert summary["categories"] == {"coding": 1, "writing": 1}


def test_summarize_empty_library():
    assert summarize_library([]) == {
        "count": 0,
        "average_score": 0.0,
        "highest_scoring": None,
        "categories": {},
    }


def test_update_prompt_record_preserves_identity_and_refreshes_score():
    original = create_prompt_record(
        "Draft",
        "Writing",
        "Write a summary.",
        record_id="fixed-id",
        created_at="2026-07-18T12:00:00+00:00",
    )

    updated = update_prompt_record(
        original,
        title="  Improved Draft  ",
        category="ACADEMIC",
        text=(
            "Act as an editor. Context: the reader is a student. "
            "Summarize the article. You must use five bullets. "
            "Return Markdown. Example: one fact per bullet. Ensure accuracy."
        ),
        updated_at="2026-07-20T09:30:00+00:00",
    )

    assert updated["id"] == "fixed-id"
    assert updated["created_at"] == "2026-07-18T12:00:00+00:00"
    assert updated["updated_at"] == "2026-07-20T09:30:00+00:00"
    assert updated["title"] == "Improved Draft"
    assert updated["category"] == "academic"
    assert updated["score"] > original["score"]
    assert original["title"] == "Draft"


def test_update_prompt_record_defaults_empty_category_to_general():
    record = create_prompt_record("Draft", "writing", "Write a summary.")
    updated = update_prompt_record(record, category="   ")
    assert updated["category"] == "general"


def test_update_prompt_record_rejects_no_changes():
    record = create_prompt_record("Draft", "writing", "Write a summary.")
    with pytest.raises(ValueError, match="At least one change"):
        update_prompt_record(record)


def test_search_records_filters_and_sorts():
    records = [
        create_prompt_record(
            "Beta Coding",
            "coding",
            "Write Python code.",
            record_id="b",
            created_at="2026-07-18T12:00:00+00:00",
        ),
        create_prompt_record(
            "Alpha Writing",
            "writing",
            (
                "Act as an editor. Context: students. Analyze this draft. "
                "You must preserve facts. Return Markdown. Example: use bullets. "
                "Ensure correctness."
            ),
            record_id="a",
            created_at="2026-07-19T12:00:00+00:00",
        ),
        create_prompt_record(
            "Gamma Coding",
            "coding",
            "Explain recursion for a beginner.",
            record_id="c",
            created_at="2026-07-20T12:00:00+00:00",
        ),
    ]

    matched = search_records(
        records,
        query="python",
        category="CODING",
        sort_by="title",
        descending=False,
    )
    assert [record["id"] for record in matched] == ["b"]

    by_score = search_records(records, sort_by="score", descending=True)
    assert by_score[0]["id"] == "a"

    by_title = search_records(records, sort_by="title", descending=False)
    assert [record["title"] for record in by_title] == [
        "Alpha Writing",
        "Beta Coding",
        "Gamma Coding",
    ]


def test_search_records_rejects_unknown_sort():
    with pytest.raises(ValueError, match="Unsupported sort field"):
        search_records([], sort_by="unknown")


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        ({"not": "a list"}, "JSON list"),
        ([{"id": "x"}], "incomplete"),
        (
            [
                {
                    "id": "x",
                    "title": 123,
                    "category": "coding",
                    "text": "Write code.",
                    "created_at": "2026-07-18T12:00:00+00:00",
                    "updated_at": "2026-07-18T12:00:00+00:00",
                    "score": 20,
                }
            ],
            "title",
        ),
        (
            [
                {
                    "id": "x",
                    "title": "One",
                    "category": "coding",
                    "text": "Write code.",
                    "created_at": "not-a-time",
                    "updated_at": "2026-07-18T12:00:00+00:00",
                    "score": 20,
                }
            ],
            "timestamp",
        ),
        (
            [
                {
                    "id": "x",
                    "title": "One",
                    "category": "coding",
                    "text": "Write code.",
                    "created_at": "2026-07-18T12:00:00+00:00",
                    "updated_at": "2026-07-18T12:00:00+00:00",
                    "score": 101,
                }
            ],
            "score",
        ),
    ],
)
def test_load_library_rejects_invalid_schema(tmp_path, payload, message):
    path = tmp_path / "invalid.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match=message):
        load_library(path)


def test_load_library_rejects_duplicate_ids(tmp_path):
    first = create_prompt_record("One", "general", "Write one.", record_id="same")
    second = create_prompt_record("Two", "general", "Write two.", record_id="same")
    path = tmp_path / "duplicates.json"
    path.write_text(json.dumps([first, second]), encoding="utf-8")

    with pytest.raises(ValueError, match="duplicate ID"):
        load_library(path)


def test_cli_list_filters_by_category(tmp_path, capsys):
    data_file = tmp_path / "library.json"
    save_library(
        data_file,
        [
            create_prompt_record(
                "Coding One", "Coding", "Write Python code.", record_id="c1"
            ),
            create_prompt_record(
                "Writing One", "writing", "Write a summary.", record_id="w1"
            ),
        ],
    )

    assert main(["--data-file", str(data_file), "list", "--category", "CODING"]) == 0
    output = capsys.readouterr().out
    assert "Coding One" in output
    assert "Writing One" not in output


def test_cli_add_search_show_edit_export_delete_workflow(tmp_path, capsys):
    data_file = tmp_path / "library.json"
    report_file = tmp_path / "exports" / "analysis.md"

    assert (
        main(
            [
                "--data-file",
                str(data_file),
                "add",
                "--title",
                "Draft Summary",
                "--category",
                "Writing",
                "--prompt",
                "Write a summary.",
            ]
        )
        == 0
    )
    add_output = capsys.readouterr().out
    match = re.search(r"ID ([0-9a-f]+)", add_output)
    assert match is not None
    record_id = match.group(1)

    assert (
        main(
            [
                "--data-file",
                str(data_file),
                "list",
                "--query",
                "summary",
                "--sort",
                "title",
                "--ascending",
            ]
        )
        == 0
    )
    assert "Draft Summary" in capsys.readouterr().out

    assert main(["--data-file", str(data_file), "show", record_id]) == 0
    show_output = capsys.readouterr().out
    assert "Prompt: " in show_output
    assert "Write a summary." in show_output

    improved = (
        "Act as an editor. Context: the audience is a student. "
        "Summarize the source. You must use five bullets. Return Markdown. "
        "Example: one fact per bullet. Ensure accuracy and completeness."
    )
    assert (
        main(
            [
                "--data-file",
                str(data_file),
                "edit",
                record_id,
                "--title",
                "Improved Summary",
                "--category",
                "Academic",
                "--prompt",
                improved,
            ]
        )
        == 0
    )
    edit_output = capsys.readouterr().out
    assert "Updated 'Improved Summary'" in edit_output

    assert (
        main(
            [
                "--data-file",
                str(data_file),
                "export",
                record_id,
                "--output",
                str(report_file),
            ]
        )
        == 0
    )
    capsys.readouterr()
    report = report_file.read_text(encoding="utf-8")
    assert "# Prompt Analysis: Improved Summary" in report
    assert "## Suggested Improvements" in report

    assert main(["--data-file", str(data_file), "delete", record_id, "--yes"]) == 0
    assert "Deleted 'Improved Summary'." in capsys.readouterr().out
    assert load_library(data_file) == []


def test_cli_edit_requires_a_change(tmp_path, capsys):
    data_file = tmp_path / "library.json"
    record = create_prompt_record(
        "Draft", "general", "Write a summary.", record_id="abc"
    )
    save_library(data_file, [record])

    assert main(["--data-file", str(data_file), "edit", "abc"]) == 1
    error = capsys.readouterr().err
    assert "At least one change" in error


def test_create_prompt_record_rejects_invalid_timestamp():
    with pytest.raises(ValueError, match="created_at timestamp"):
        create_prompt_record(
            "Draft",
            "general",
            "Write a summary.",
            created_at="not-a-timestamp",
        )


def test_save_library_rejects_duplicate_ids_before_writing(tmp_path):
    path = tmp_path / "library.json"
    records = [
        create_prompt_record("One", "general", "Write one.", record_id="same"),
        create_prompt_record("Two", "general", "Write two.", record_id="same"),
    ]

    with pytest.raises(ValueError, match="duplicate ID"):
        save_library(path, records)

    assert not path.exists()


def test_save_library_rejects_invalid_record_before_writing(tmp_path):
    path = tmp_path / "library.json"
    invalid = {
        "id": "x",
        "title": "Draft",
        "category": "general",
        "text": "Write a summary.",
        "created_at": "2026-07-20T09:00:00+00:00",
        "updated_at": "2026-07-20T09:00:00+00:00",
        "score": "bad",
    }

    with pytest.raises(ValueError, match="score"):
        save_library(path, [invalid])

    assert not path.exists()


def test_create_prompt_record_rejects_timestamp_without_timezone():
    with pytest.raises(ValueError, match="timezone"):
        create_prompt_record(
            "Draft",
            "general",
            "Write a summary.",
            created_at="2026-07-20T09:00:00",
        )
