import sys
from datetime import date

# pyrefly: ignore [missing-import]
import inflect

MINUTES_PER_DAY = 24 * 60


def main():
    birth_date = input("Date of Birth: ")

    try:
        birthday = parse_date(birth_date)
        minutes = calculate_minutes(birthday)
    except ValueError:
        sys.exit("Invalid date")

    print(format_minutes(minutes))


def parse_date(value: str) -> date:
    """Convert a YYYY-MM-DD string into a date object."""
    return date.fromisoformat(value)


def calculate_minutes(birthday: date, today: date | None = None) -> int:
    """Return the number of whole minutes between two dates."""
    if today is None:
        today = date.today()

    if birthday > today:
        raise ValueError("Birth date cannot be in the future")

    difference = today - birthday
    return difference.days * MINUTES_PER_DAY


def format_minutes(minutes: int) -> str:
    """Convert a number of minutes into the required English sentence."""
    engine = inflect.engine()
    words = engine.number_to_words(minutes, andword="")

    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
