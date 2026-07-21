# Road to AI Engineer

An active development workspace for course exercises, experiments, and portfolio-oriented AI/software engineering work. The repository is organized around independent units of work; it is not a single application and does not use one shared dependency environment.

## Start Work

1. Open `Road to AI Engineer.code-workspace` in VS Code.
2. Read `CURRENT_WORK.md` for the exact current task, path, output, and completion rule.
3. Use `ROADMAP.md` to map the Notion Life OS calendar to the correct codebase.
4. Run tests from the relevant course exercise or project root, not from the repository root.

## Architecture

The repository uses a hybrid stage structure. Course-required layouts stay intact inside each stage. Independent portfolio applications remain separate Git repositories and are exposed through the multi-root VS Code workspace.

| Stage | Development focus | Current state |
|---|---|---|
| `stage-01-cs-foundations/` | Git/GitHub and CS foundations | Historical reference |
| `stage-02-python-software-design/` | CS50P, Python exercises, software-design notes | CS50P completed; design videos ongoing |
| `stage-03-data-structures-algorithms/` | Historical DSA course work and independent LeetCode | Structured curriculum retired; practice self-directed |
| `stage-04-data-scientific-python/` | NumPy, pandas, Matplotlib, SciPy | Planned |
| `stage-05-machine-learning/` | CS50 AI, ML foundations, model projects | Active: CS50 AI |
| `stage-06-backend-infrastructure/` | APIs, Docker, databases, deployment | Planned |
| `stage-07-ai-engineering/` | Hugging Face, LLMs, RAG, agents | Planned |
| `stage-08-security-specialization/` | AI security and portfolio hardening | Deferred |

## Active Work Units

| Unit | Location | Type | Status | Primary verification |
|---|---|---|---|---|
| CS50 AI | `stage-05-machine-learning/CS50AI/` | Course and projects | Active | Course-specific checks per project |
| AI Prompt Optimizer | `../aiprompts-optimizer/` | Independent portfolio project | Active external repository | `backend/venv/Scripts/python.exe -m pytest -q` |
| WC2026 Predictor | `../wc2026-predictor/` | Independent ML project and technical curriculum | Active external repository with local uncommitted data | Project-specific tests; preserve current working tree |
| PromptVault | `stage-02-python-software-design/CS50P/Final Project/promptvault_cs50p_final_project/` | Completed CS50P final project | Completed | `python -m pytest -q` |

## Environment Rules

- Keep dependencies local to each project or course work unit.
- Preserve official grader filenames and distribution structures.
- Do not treat stage directories as shared Python import roots.
- Use relative repository paths in committed configuration.
- Keep secrets in ignored environment files; commit only templates such as `.env.example`.
- Generated caches and native build artifacts are ignored. Six historical `.exe` files remain tracked pending explicit approval to remove them.

## Development Commands

PromptVault:

```powershell
cd "stage-02-python-software-design\CS50P\Final Project\promptvault_cs50p_final_project"
python -m pytest -q
```

C syntax check without generating a binary:

```powershell
gcc -fsyntax-only "path\to\exercise.c"
```

Run the historical linear-search exercise:

```powershell
.\run-search.ps1
```

## Planning Source

The Notion Life OS calendar is the daily scheduling source of truth. `ROADMAP.md` contains only the stable mapping from scheduled work to code paths. `CURRENT_WORK.md` is the short operational handoff for the current day.

## Repository

- Remote: https://github.com/veselinkalinov/AIEngineeringRoadmap
- License: MIT
