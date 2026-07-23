# PromptVault
#### Description:

PromptVault is a command-line tool for storing, analyzing, and comparing prompts for AI systems. It's my CS50P final project, written in Python, and it runs entirely offline — no API key, no account, no external database. Everything lives in a local JSON file you can open and read yourself.

I built this because my own prompt drafts were scattered across ChatGPT history, random text files, and half-remembered notes. If I wanted to compare an old version of a prompt against a rewrite, or check whether I'd forgotten to specify an output format, there was nowhere to look. PromptVault fixes that: one library, stable IDs, timestamps, categories, and a score for each prompt so I can tell at a glance whether it's actually well-structured or just long.

The scoring itself is intentionally simple. It doesn't try to judge whether a prompt is "good" in some deep sense — it checks for seven concrete things: a role, context, a task, constraints, an output format, examples, and success criteria, plus basic stats like word count and sentence length. Each dimension has a fixed weight, so the same prompt gets the same score every time. Testing a heuristic that never changes its mind is a lot easier than testing something that might.

## Features

- Add a prompt directly, from a file, or by typing it into the terminal.
- List, search, filter by category, and sort by date, title, category, or score.
- Show the full text and metadata of any saved prompt.
- Edit title, category, or text — any combination, without touching the others.
- Analyze a saved or unsaved prompt and see which dimensions it's missing.
- Get specific suggestions for what to add.
- Compare two saved prompts side by side.
- Generate a structured prompt template from a role, goal, context, and constraints, and optionally save it straight to the library.
- Pull up library-wide stats: average score, category breakdown, top scorer.
- Export a full Markdown report for any prompt.
- Delete a prompt, with or without a confirmation prompt.

## Project Files

### `project.py`

The required main file. `main()`, the argument parser, every command handler, and the actual logic — validation, scoring, persistence — all live here.

The functions that matter most if you're reading the code:

- `normalize_prompt(text)` — cleans up line endings, trailing whitespace, and repeated blank lines.
- `analyze_prompt(text)` — runs the seven-dimension check and returns the score.
- `calculate_score(analysis)` — turns the detected dimensions into a 0–100 number.
- `generate_suggestions(analysis)` — turns missing dimensions into plain-English advice.
- `build_prompt_template(...)` — assembles a Markdown prompt from its parts.
- `create_prompt_record(...)` / `update_prompt_record(...)` — validate and build (or rebuild) a record, keeping the ID and creation timestamp stable across edits.
- `search_records(...)` — filters and sorts without mutating the original list.
- `load_library(path)` / `save_library(path, records)` — the JSON read/write boundary, with validation on both ends.
- `compare_prompts(first_text, second_text)` — diffs two analyses.
- `summarize_library(records)` — count, average score, top prompt, category counts.

### `test_project.py`

The pytest suite — normalization, scoring, suggestions, templates, record creation and editing, search and sort, JSON round-trips, corrupted data, duplicate IDs, comparisons, stats, and a full add → search → show → edit → export → delete run through the CLI. Everything that touches the filesystem uses pytest's `tmp_path`, so running the tests never touches a real prompt library.

### `requirements.txt`

Just pytest. The app itself only needs the standard library.

### `VIDEO_SCRIPT.md`

Notes for the demo recording — order of commands, what to say, a checklist so I don't ramble past three minutes.

### `SUBMISSION_CHECKLIST.md`

What's done versus what still needs a human: recording the video, uploading it, swapping in the real URL, running `submit50`.

### `REQUIREMENTS_MATRIX.md`

Maps each CS50P requirement to where it's actually implemented, so it's easy to check nothing's missing before submitting.

### `VERIFICATION.txt`

A log of the commands I actually ran to confirm things work, and what they returned. Needs regenerating if the code changes.

### `.gitignore`

Keeps Python/pytest caches, local `.json` libraries, `.tmp` files from the atomic writes, the virtualenv, and export output out of version control.

## Installation

Needs Python 3.10+. From the project root:

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Then:

```bash
python -m pip install -r requirements.txt
```

You only need pytest installed if you want to run the tests — the app runs fine without it.

## Basic Usage

```bash
python project.py --help
```

Add a prompt directly:

```bash
python project.py add --title "Python Review" --category coding --prompt "Act as a Python reviewer. Analyze the code, preserve comments, return a Markdown table, and ensure every finding is correct."
```

From a file:

```bash
python project.py add --title "File Prompt" --category writing --file prompt.txt
```

List everything:

```bash
python project.py list
```

Search and sort:

```bash
python project.py list --query recursion --category coding --sort score
```

```bash
python project.py list --sort title --ascending
```

Show one, using the ID `add` or `list` printed for you:

```bash
python project.py show PROMPT_ID
```

Edit it:

```bash
python project.py edit PROMPT_ID --title "Improved Python Review" --category academic --prompt "Act as a senior Python reviewer. Context: the code is for a beginner. Review it for correctness. Do not remove comments. Return a Markdown table. Example columns: issue, reason, fix. Ensure every finding is verified."
```

Analyze or get suggestions for a saved prompt:

```bash
python project.py analyze --id PROMPT_ID
python project.py suggest --id PROMPT_ID
```

Or analyze text you haven't saved yet:

```bash
python project.py analyze --prompt "Write a summary."
```

Build and save a template:

```bash
python project.py template --role "Act as a tutor." --goal "Explain recursion." --context "The learner knows basic Python." --constraint "Use one code example." --constraint "Avoid advanced mathematics." --output "Return three Markdown sections." --save-title "Recursion Tutor"
```

Compare two saved prompts:

```bash
python project.py compare FIRST_ID SECOND_ID
```

Stats and export:

```bash
python project.py stats
python project.py export PROMPT_ID --output exports/prompt-report.md
```

Delete without the confirmation prompt:

```bash
python project.py delete PROMPT_ID --yes
```

`--data-file` lets you point at a different library, but it has to come before the command:

```bash
python project.py --data-file demo_library.json list
```

## Data Storage Format

By default everything goes in `prompt_library.json` in the working directory — a JSON list, one object per record:

```json
{
  "id": "a1b2c3d4e5f6",
  "title": "Python Review",
  "category": "coding",
  "text": "Act as a Python reviewer...",
  "created_at": "2026-07-20T09:30:00+00:00",
  "updated_at": "2026-07-20T09:30:00+00:00",
  "score": 73
}
```

IDs have to be unique. Title, category, and text can't be empty, and text tops out at 20,000 characters. Timestamps need a timezone offset, and `updated_at` can't be earlier than `created_at`. Scores are integers from 0 to 100. Every load and save runs full validation, so bad JSON, missing fields, wrong types, broken timestamps, out-of-range scores, or duplicate IDs raise a clear error instead of quietly corrupting the file.

Writes go to a temp file first, then get swapped in with `os.replace`, so an interrupted write can't leave you with a half-written JSON file.

## Validation and Error Handling

Anything expected — an unknown ID, an empty title, an edit with nothing to change, a file that can't be read, broken JSON, duplicate IDs, an output path that can't be written — gets caught in `main()`, printed to stderr with an `Error:` prefix, and returns a non-zero exit code.

A missing library file isn't an error; it just means the library is new, so the first `add` creates it. Tests never touch a real library, since they all write to `tmp_path`.

## Testing

```bash
python -m pytest
```

```bash
python -m compileall .
```

The suite covers the normal cases plus the annoying ones: empty input, malformed data, bad timestamps and scores, duplicate IDs, missing files, filtering and sorting, persistence, the Markdown export, and a full CLI run from add through delete.

## Design Decisions and Tradeoffs

I went with JSON instead of SQLite because this is a single-user CLI tool with a small library — JSON is something I can open in a text editor and actually read during a demo. SQLite would give better querying at scale, but that's not a problem I have here, and the schema/migration overhead isn't worth it for this scope.

I also went with plain keyword heuristics instead of calling an LLM to grade the prompts. An AI judge might understand meaning better, but then I'd need an API key, internet access, and a way to mock all of that in tests — and the results wouldn't be reproducible run to run. The heuristic is dumber, but it's honest about being dumb, and it behaves the same way every time.

Everything stays in `project.py` because CS50P wants the main function and the required helper functions in that one file, and the project is still small enough that this doesn't get messy. That said, the logic is still separated by concern — the analysis functions don't know about the CLI, persistence has its own boundary, and the command handlers just wire things together.

## Limitations

The score is a heuristic, not a real measure of prompt quality — a prompt can contain the word "example" without containing a useful one, and a short, sharp prompt can score lower than a bloated one that happens to hit every keyword. PromptVault also doesn't run prompts against any model, sync across devices, handle concurrent writers, encrypt anything, or have a GUI. None of that was in scope.

## Possible Future Improvements

Tags, an optional SQLite backend, automatic backups, CSV import/export, version history per prompt, configurable scoring weights, maybe a TUI at some point. None of it made the cut for the submission — better to hand in something small that works than something bigger that's half done.

Before submitting: replace `<ADD VIDEO URL AFTER RECORDING>` with the real link, and only after the video is actually recorded and uploaded.
