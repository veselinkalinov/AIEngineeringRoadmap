import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = (
        r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) "
        r"to "
        r"(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$"
    )

    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError

    start_hour, start_minutes, start_period, end_hour, end_minutes, end_period = (
        match.groups()
    )

    start_time = convert_time(start_hour, start_minutes, start_period)
    end_time = convert_time(end_hour, end_minutes, end_period)

    return f"{start_time} to {end_time}"


def convert_time(hour, minutes, period):
    hour = int(hour)

    if minutes is None:
        minutes = "00"

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minutes}"


if __name__ == "__main__":
    main()
