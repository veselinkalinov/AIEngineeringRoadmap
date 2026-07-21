# CS50's Introduction to Programming with Python

- Provider: Harvard University / CS50
- Official course: https://cs50.harvard.edu/python/
- Status: Completed on 2026-07-20
- Certificate: Earned; certificate artifact is not stored in this repository
- Roadmap role: Python foundation before CS50 AI and applied AI/ML engineering

## Structure

- `Week 0 - Functions/` through `Week 9 - Et Cetera/` preserve lecture, short, and problem-set filenames.
- `Final Project/promptvault_cs50p_final_project/` is the completed portfolio-grade course project.
- Exercise directories are independent grader units. Run tests from the directory containing the matching `test_*.py` file.

## Validated Project

PromptVault requires Python 3.10 or newer.

```powershell
cd "Final Project\promptvault_cs50p_final_project"
python -m pip install -r requirements.txt
python -m pytest -q
```

Expected result on 2026-07-21: `33 passed`.

## Known Course-Example Constraints

- `Week 5 - Unit Tests/Lecture/calculator.py` intentionally demonstrates a failing implementation; its tests are not a repository regression suite.
- `Week 8 - Object-Oriented Programming/Problem Set 8/Seasons of Love` requires the course dependency `inflect` before its tests can be collected.
- Keep official problem-set filenames unchanged for grading and historical traceability.
