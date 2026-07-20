# PromptVault Requirements Matrix

| Requirement | Implementation location | Verification method | Status |
|---|---|---|---|
| Implemented in Python | `project.py` | File inspection and compilation | PASS |
| Root `project.py` | Project root | Final file-tree inspection | PASS |
| Module-level `main()` | `project.py` | AST inspection and CLI execution | PASS |
| At least three additional module-level custom functions | `project.py` | AST inspection | PASS |
| Executable entry point | Bottom of `project.py` | Source inspection and subprocess execution | PASS |
| Root `test_project.py` | Project root | Final file-tree inspection | PASS |
| Matching pytest tests for at least three custom functions | `test_project.py` | Test-name and import inspection | PASS |
| Meaningful normal and edge-case tests | `test_project.py` | Full pytest execution | PASS |
| Deterministic tests without network dependencies | `test_project.py` | Test review and isolated temporary paths | PASS |
| Substantial complexity | Full CLI and persistence workflows | Feature review and integration workflow | PASS |
| Input validation and intentional error handling | Record functions, persistence functions, `main()` | Invalid JSON/schema/duplicate/edit tests | PASS |
| Persistent local data | `load_library`, `save_library` | Round-trip and CLI integration tests | PASS |
| Creation/read/update/delete workflows | `add`, `show`, `edit`, `delete` commands | End-to-end CLI test and manual workflow | PASS |
| Search/filter/sort/report workflows | `search_records`, `list`, `stats`, `export` | Unit and CLI tests | PASS |
| Root `requirements.txt` | Project root | Dependency/import review | PASS |
| No standard-library modules in requirements | `requirements.txt` | Manual dependency review | PASS |
| Root `README.md` | Project root | File-tree and content inspection | PASS |
| Required README heading structure | Top of `README.md` | Exact text inspection | PASS |
| Literal video placeholder until recording | Top of `README.md` | Placeholder scan | PASS |
| Detailed description and file explanations | `README.md` | Word count and content review | PASS |
| Installation, usage, and tests documented | `README.md` | Command review and execution | PASS |
| Data format, validation, design decisions, limitations, future work documented | `README.md` | Content inspection | PASS |
| Video script no longer than three minutes | `VIDEO_SCRIPT.md` | Script and sequence review | PASS |
| Personal opening-screen placeholders | `VIDEO_SCRIPT.md` | Exact placeholder inspection | PASS |
| Final pytest command | Entire project | `python -m pytest` | PASS |
| Final compilation command | Entire project | `python -m compileall .` | PASS |
| Complete realistic workflow | CLI with isolated JSON file | Subprocess workflow | PASS |
| No credentials or secrets | Entire project | Pattern scan and file review | PASS |
| Real video URL | Student recording/upload | Not project-controlled | MANUAL ACTION REQUIRED |
| Video recording and upload | Student action | Manual playback check | MANUAL ACTION REQUIRED |
| CS50 form and `submit50` | Student/external service | External submission | MANUAL ACTION REQUIRED |
| Gradebook opening | Student/external service | External action | MANUAL ACTION REQUIRED |
