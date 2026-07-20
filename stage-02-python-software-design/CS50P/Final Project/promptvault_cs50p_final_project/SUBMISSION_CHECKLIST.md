# CS50P Final Project Submission Checklist

## Deadline

The supplied project requirements state the deadline as:

```text
Friday, January 1, 2027 at 12:59 AM GMT+1
```

## Verified Project-Controlled Requirements

- [x] The project is implemented in Python.
- [x] `project.py` is in the project root.
- [x] `project.py` contains a module-level `main()` function.
- [x] `project.py` contains more than three additional meaningful module-level custom functions.
- [x] The executable `if __name__ == "__main__"` entry point exists.
- [x] `test_project.py` is in the project root.
- [x] More than three custom functions have matching meaningful pytest tests.
- [x] Tests cover normal, boundary, invalid-data, persistence, and CLI integration behavior.
- [x] `requirements.txt` contains only the required pip-installable dependency.
- [x] `README.md` contains the required heading structure and literal video placeholder.
- [x] The README documents installation, usage, tests, files, data, validation, design decisions, limitations, and future work.
- [x] The project is substantially larger than an individual CS50P problem set.
- [x] The application does not require a network service, account, API key, or unavailable hardware.
- [x] The final verification commands and results are recorded in `VERIFICATION.txt`.

## Student Review Before Recording

- [ ] Read and understand all of `project.py`.
- [ ] Read and understand all tests in `test_project.py`.
- [ ] Run every primary command yourself.
- [ ] Confirm that the implementation accurately represents work you can explain and defend.
- [ ] Remove any personal demo data created during practice.
- [ ] Run the final checks in your own submission environment.

## Video Actions

- [ ] Fill in the personal placeholders in `VIDEO_SCRIPT.md` for the recording screen.
- [ ] Record a demonstration no longer than three minutes.
- [ ] Include project title, name, GitHub username, edX username, city/country, and recording date at the beginning.
- [ ] Upload the video as public or unlisted, not private.
- [ ] Play the uploaded video from beginning to end.
- [ ] Replace `<ADD VIDEO URL AFTER RECORDING>` in `README.md` with the real URL.

## Submission Actions

- [ ] Complete the required CS50 submission form.
- [ ] From the project root, run:

```bash
submit50 cs50/problems/2022/python/project
```

- [ ] Read the `submit50` output and confirm the intended files were submitted.
- [ ] Open the CS50P gradebook after submission so completion and certificate processing can be triggered.

## Final Commands to Run Locally

```bash
python -m pytest
python -m compileall .
python project.py --help
```
