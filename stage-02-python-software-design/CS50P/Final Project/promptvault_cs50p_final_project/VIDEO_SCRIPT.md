# PromptVault — Codex Voiceover and Video Production Goal

## Purpose

Use this file as the authoritative production brief for creating the voiceover and preparing the demonstration of **PromptVault**, a CS50P final project.

This is an execution-oriented brief. Do not merely summarize the instructions or return a rewritten script. Inspect the project, verify the demonstrated commands, prepare the narration assets, and generate the voiceover when a supported speech-synthesis tool is available.

The finished CS50P demonstration must be **three minutes or less**. Target a final duration of **2 minutes 35 seconds to 2 minutes 50 seconds**, leaving a small safety margin for transitions and rendering differences.

---

# 1. Required Codex Deliverables

Create the following production assets without modifying `project.py`, `test_project.py`, or the project’s behavior:

1. `voiceover_script_final.txt`
   - Contains only the words that should be spoken.
   - Excludes headings, timecodes, Markdown syntax, stage directions, commands, and placeholders.

2. `voiceover_cues.md`
   - Maps each narration section to the corresponding screen action.
   - Includes approximate start and end times.

3. `voiceover.wav`
   - Preferred master format: PCM WAV, 48 kHz, 16-bit or 24-bit, mono.
   - Generate this only if an available tool can create it reliably.

4. `voiceover.mp3`
   - Delivery copy encoded at 192 kbps or better.
   - Generate it from the final approved narration rather than from an earlier draft.

5. `video_demo_commands.txt`
   - Contains the exact verified commands used for the demonstration.
   - Replaces temporary prompt IDs with the real IDs created during rehearsal.

6. `voiceover_verification.md`
   - Records the voice used, tool used, output duration, file formats, and quality checks.
   - Reports any blocked deliverable honestly instead of claiming it was created.

Do not add voice-generation packages to `requirements.txt`. Voiceover tooling is a production aid, not a runtime dependency of PromptVault.

---

# 2. Hard Constraints

- The final video must not exceed **3:00**.
- The narration should ideally be **2:05–2:20**, excluding the silent opening title card and brief closing hold.
- Do not invent a student name, GitHub username, edX username, city, country, recording date, video URL, test result, command result, or generated file.
- Do not speak placeholder markers such as `<ADD STUDENT NAME>`.
- Do not expose private prompts, credentials, API keys, personal file paths, account information, or unrelated terminal history.
- Do not claim that the video was recorded, uploaded, or submitted unless that action actually occurred.
- Do not change project source code merely to make the demonstration easier.
- Do not use an online service that requires uploading private project data unless the user explicitly authorizes it.
- Do not include background music unless the user explicitly requests it.
- Do not use a dramatic, advertising-style, overly emotional, or robotic delivery.
- Do not pronounce punctuation, Markdown symbols, command flags, or stage directions unless the narration explicitly calls for them.
- Keep the narration factual and limited to features that exist in the current repository.

---

# 3. Preflight Verification

Before creating the voiceover, Codex must:

1. Inspect these files:
   - `project.py`
   - `test_project.py`
   - `README.md`
   - `requirements.txt`
   - this `VIDEO_SCRIPT.md`

2. Verify the CLI help:

```bash
python project.py --help
```

3. Verify the automated tests:

```bash
python -m pytest -q
```

4. Verify compilation:

```bash
python -m compileall project.py test_project.py
```

5. Rehearse the complete demo using a disposable file named `video_demo.json`.

6. Remove any old rehearsal artifacts before starting:

```bash
python -c "from pathlib import Path; [p.unlink() for p in [Path('video_demo.json'), Path('exports/video-report.md')] if p.exists()]"
```

7. Capture the real IDs printed by the `add` and `template` commands.

8. Replace `<FIRST_ID>` and `<SECOND_ID>` in the rehearsal command list with those real IDs.

9. Confirm that every narrated claim matches observed program behavior.

If a command fails, diagnose and report the exact failure. Do not work around it by narrating a feature that was not demonstrated successfully.

---

# 4. Voice and Delivery Specification

## Voice profile

Use a clear, natural English voice with these characteristics:

- neutral international or lightly American/British-accented English;
- calm and technically confident;
- friendly but not informal;
- appropriate for a university project demonstration;
- consistent volume and pacing;
- no exaggerated excitement;
- no vocal fry, whispering, or theatrical emphasis.

## Speaking rate

- Target **140–150 words per minute**.
- Do not exceed **155 words per minute**.
- Use short natural pauses between major workflows.
- Add approximately **250–400 ms** of silence between sections.
- Add approximately **500 ms** before the final sentence.

## Pronunciation guide

Use these pronunciations consistently:

- **PromptVault** — “Prompt Vault”
- **CS50P** — “C S fifty P”
- **Python** — standard English pronunciation
- **JSON** — “Jason”
- **pytest** — “pie test”
- **Markdown** — “mark-down”
- **CLI** — “C L I”
- **ISO 8601** — “I S O eighty-six oh one”
- **UTF-8** — “U T F eight”

Do not read filenames character by character. Say “project dot pie,” “test project dot pie,” and “requirements dot text” only when the script explicitly mentions them.

---

# 5. Audio Production Requirements

Use the best available local or connected speech-synthesis capability. Inspect the available tools before choosing one.

When audio generation is available:

1. Generate the entire narration from `voiceover_script_final.txt`.
2. Prefer one continuous take to avoid audible voice changes.
3. Use paragraph breaks or SSML pauses only when supported reliably.
4. Do not add unsupported emotion tags, sound effects, or music.
5. Trim excessive leading silence while preserving approximately 300 ms before the first word.
6. Preserve approximately 500–800 ms of silence after the final word.
7. Normalize the final audio to approximately **-16 LUFS integrated** for a spoken online video.
8. Keep true peak at or below approximately **-1 dBTP**.
9. Avoid clipping, pumping, abrupt cuts, background noise, and audible synthesis artifacts.
10. Export both WAV and MP3 when the toolchain supports them.
11. Measure the final duration rather than estimating it.
12. Listen to or inspect the complete generated file before declaring it ready.

When direct speech generation is unavailable:

- still create `voiceover_script_final.txt`, `voiceover_cues.md`, and `voiceover_verification.md`;
- state that audio generation is blocked by the current environment;
- provide an exact command or next action for a supported tool;
- do not create an empty, silent, corrupted, or falsely labelled audio file.

---

# 6. Opening Title Card

Display this card for approximately **7–9 seconds** before the main screen recording.

```text
PromptVault
CS50P Final Project

Student: Veselin
GitHub: https://github.com/veselinkalinov
edX: vesko_kalinov06
Location: Varna, Bulgaria
Recorded: 20.07.2026
```

Rules:

- Replace every placeholder before recording.
- Keep the title card silent, or begin the first narration sentence during its final two seconds.
- Use a plain, readable layout with high contrast.
- Do not show a fake or placeholder video URL.

---

# 7. Canonical Voiceover Script

The following block is the **only canonical narration**. Codex must copy only its spoken sentences into `voiceover_script_final.txt`. Do not copy the heading, quotation marks, timing labels, or stage directions.

## Narration — target approximately 2 minutes 5 seconds to 2 minutes 20 seconds

> PromptVault is my CS50P final project. It is an offline Python command-line application for storing, organizing, evaluating, and improving prompts for generative AI systems.
>
> The program uses a local JSON file, so it does not need an API key, external database, paid service, or internet connection. Each saved prompt receives a stable identifier, timestamps, a category, and a deterministic quality score.
>
> I will begin with the help screen, which shows the available commands. I then add a deliberately short prompt. PromptVault validates the input, saves it atomically, and calculates its score.
>
> Next, I generate a structured prompt template. The template combines a role, goal, context, constraints, output format, and success criteria. I save it as a second record so the two approaches can be compared.
>
> The list command can search across prompt text and metadata, filter by category, and sort results. The show command displays the complete saved record.
>
> PromptVault’s analyzer checks seven transparent dimensions: role, context, task, constraints, output format, examples, and success criteria. The suggestion command identifies missing dimensions and explains how the prompt can be improved.
>
> I now edit the short prompt into a more complete version. The record keeps its original identifier and creation time, while its updated timestamp and quality score are recalculated. The comparison command then shows the score difference and which dimensions changed.
>
> The statistics command summarizes the local library. The export command creates a readable Markdown report containing the prompt, metrics, detected dimensions, and improvement suggestions.
>
> The program also handles missing files, invalid input, damaged JSON, duplicate identifiers, invalid timestamps, and unknown records with clear errors instead of uncontrolled crashes.
>
> The required application is implemented in project dot pie. Test project dot pie contains deterministic pytest coverage for the core functions, persistence, validation, and a complete command-line workflow.
>
> This is PromptVault, my CS50P final project.

Do not alter technical claims unless project verification shows that the implementation has changed.

---

# 8. Detailed Cue Sheet

The timings below are targets, not fabricated results. Adjust them after measuring the actual narration.

| Target time | Screen action | Narration section |
|---|---|---|
| `0:00–0:08` | Opening title card | First sentence may start near `0:06` |
| `0:08–0:22` | Show project root and `python project.py --help` | Project purpose and offline design |
| `0:22–0:38` | Run the `add` command | Stable ID, validation, atomic save, score |
| `0:38–0:55` | Run the `template` command | Structured template components |
| `0:55–1:10` | Run `list`, then `show` | Search, filtering, sorting, full record |
| `1:10–1:31` | Run `analyze` and `suggest` | Seven dimensions and suggestions |
| `1:31–1:53` | Run `edit`, `show`, and `compare` | Update behavior and comparison |
| `1:53–2:10` | Run `stats` and `export` | Summary and Markdown report |
| `2:10–2:25` | Briefly show an expected error or mention validation | Error handling |
| `2:25–2:42` | Run `python -m pytest -q` | Source and test coverage |
| `2:42–2:50` | Hold exported report or project title | Closing sentence |

Do not force a screen action to match an inaccurate timecode. Synchronize the cue sheet to the measured voiceover after generation.

---

# 9. Verified Demonstration Workflow

Run all commands from the project root. Keep the terminal window large and readable.

## Step 1 — Reset disposable demo data

```bash
python -c "from pathlib import Path; [p.unlink() for p in [Path('video_demo.json'), Path('exports/video-report.md')] if p.exists()]"
```

## Step 2 — Show help

```bash
python project.py --data-file video_demo.json --help
```

## Step 3 — Add a deliberately weak prompt

```bash
python project.py --data-file video_demo.json add --title "Short Summary" --category writing --prompt "Summarize this text."
```

Copy the printed ID and use it as `<FIRST_ID>`.

## Step 4 — Generate and save a structured prompt

```bash
python project.py --data-file video_demo.json template --role "Act as an academic editor." --goal "Summarize the supplied article." --context "The reader is a first-year university student." --constraint "Use exactly five bullets." --constraint "Do not add unsupported facts." --output "Return Markdown with a title and five bullets." --save-title "Structured Summary"
```

Copy the printed ID and use it as `<SECOND_ID>`.

## Step 5 — Search and sort

```bash
python project.py --data-file video_demo.json list --query summary --sort score
```

## Step 6 — Show the first record

```bash
python project.py --data-file video_demo.json show <FIRST_ID>
```

## Step 7 — Analyze it

```bash
python project.py --data-file video_demo.json analyze --id <FIRST_ID>
```

## Step 8 — Generate improvement suggestions

```bash
python project.py --data-file video_demo.json suggest --id <FIRST_ID>
```

## Step 9 — Edit it into a stronger prompt

```bash
python project.py --data-file video_demo.json edit <FIRST_ID> --title "Improved Summary" --category academic --prompt "Act as an academic editor. Context: the reader is a first-year university student. Summarize the supplied article. You must use exactly five bullets and must not add unsupported facts. Return Markdown with a title and five bullets. Example: include one supported fact per bullet. Ensure every statement is accurate and traceable to the source."
```

## Step 10 — Show the updated record

```bash
python project.py --data-file video_demo.json show <FIRST_ID>
```

## Step 11 — Compare both records

```bash
python project.py --data-file video_demo.json compare <FIRST_ID> <SECOND_ID>
```

## Step 12 — Show statistics

```bash
python project.py --data-file video_demo.json stats
```

## Step 13 — Export a Markdown report

```bash
python project.py --data-file video_demo.json export <FIRST_ID> --output exports/video-report.md
```

Open `exports/video-report.md` briefly in a text editor or preview pane.

## Step 14 — Demonstrate graceful failure

Use an obviously invalid record ID:

```bash
python project.py --data-file video_demo.json show does-not-exist
```

The command is expected to return a readable error and a non-zero exit status. Do not present this expected validation result as a project failure.

## Step 15 — Show the final tests

```bash
python -m pytest -q
```

Only narrate the exact number of passing tests when the number has been freshly observed. The canonical narration intentionally says “deterministic pytest coverage” without hard-coding a count.

---

# 10. Screen Recording Instructions

- Record at 1080p or higher when possible.
- Use a terminal font large enough to remain legible after upload compression.
- Prefer a dark terminal with high-contrast text or a clean light terminal.
- Hide unrelated tabs, notifications, account names, desktop files, and terminal history.
- Use a clean project path that does not reveal private usernames when possible.
- Keep mouse movement deliberate and minimal.
- Avoid long pauses while typing; paste rehearsed commands or edit out dead time.
- Do not accelerate footage so much that output becomes unreadable.
- Keep each important result visible long enough to understand.
- Zoom or crop only when it improves readability without hiding relevant context.
- Show the test result clearly near the end.
- Do not show the entire source code line by line; the video should demonstrate the project rather than become a code-reading session.

---

# 11. Synchronization and Editing Rules

1. Generate and measure the voiceover first.
2. Build the screen recording around the measured narration.
3. Cut terminal waiting time, typing delays, and irrelevant output.
4. Do not cut spoken words unnaturally.
5. Align each command result with the related narration claim.
6. Allow the viewer enough time to see IDs, scores, comparison results, the exported report, and the pytest summary.
7. Use simple cuts or short crossfades only.
8. Avoid animated transitions, excessive zooms, decorative effects, or unrelated stock footage.
9. Keep the opening card and final frame visually consistent.
10. Confirm the rendered video duration is below three minutes, not exactly three minutes.

---

# 12. Voiceover Quality-Control Checklist

Codex must verify and record each applicable item:

- [ ] The narration file contains only spoken text.
- [ ] The audio voice is consistent from beginning to end.
- [ ] PromptVault, CS50P, JSON, pytest, Markdown, and CLI are pronounced correctly.
- [ ] The speech rate remains natural and understandable.
- [ ] No placeholder is spoken.
- [ ] No command, flag, timecode, Markdown symbol, or stage direction is accidentally narrated.
- [ ] There is no clipping or obvious distortion.
- [ ] The beginning and ending are not cut off.
- [ ] The measured narration duration leaves enough room for a sub-three-minute video.
- [ ] WAV and MP3 files open and play successfully.
- [ ] The voiceover matches the final canonical script.
- [ ] Every technical statement matches verified project behavior.

---

# 13. Final Video Checklist

- [ ] Every opening-card placeholder has been replaced with real information.
- [ ] The final video is no longer than three minutes.
- [ ] The terminal text is readable at the uploaded resolution.
- [ ] No credentials, private prompts, personal paths, or unrelated data are visible.
- [ ] The video demonstrates one complete workflow.
- [ ] The analyzer and suggestion features are shown.
- [ ] Editing and comparison are shown.
- [ ] Statistics and Markdown export are shown.
- [ ] Graceful invalid-input handling is shown or clearly explained.
- [ ] The final pytest result is visible and current.
- [ ] The video was watched from beginning to end after rendering.
- [ ] The uploaded video is public or unlisted, not private.
- [ ] The uploaded copy plays successfully.
- [ ] The real video URL is added to `README.md` only after upload verification.

---

# 14. Required Codex Completion Report

After completing all possible production work, Codex must report:

## Assets Created

List every file created and its exact path.

## Voiceover Details

Report:

- synthesis tool and voice;
- language and accent;
- measured duration;
- WAV sample rate, bit depth, and channel count;
- MP3 bitrate;
- loudness or normalization method, when available.

## Verification Performed

Report the exact commands or tools used to verify:

- project behavior;
- pytest result;
- audio duration;
- audio file readability;
- final script word count;
- absence of unresolved spoken placeholders.

## Blockers

State any unavailable tool, missing personal value, or manual recording/upload step clearly. Do not mark blocked work as complete.

## Final Status

Use one of these exact statuses:

```text
VOICEOVER ASSETS COMPLETE
```

Use this only when the final script, cue sheet, WAV, MP3, and verification report were actually created and checked.

```text
VOICEOVER PREPARATION COMPLETE — AUDIO GENERATION BLOCKED
```

Use this when the script and production package are complete but the current environment cannot generate reliable audio.

```text
PARTIALLY COMPLETE — PRODUCTION BLOCKERS REMAIN
```

Use this when required project verification or production preparation remains unfinished.
