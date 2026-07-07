months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month_name, day, year = date.split(" ")

            if not day.endswith(","):
                continue

            day = day.replace(",", "")

            if month_name not in months:
                continue

            month = months.index(month_name) + 1
            day = int(day)
            year = int(year)

        if month < 1 or month > 12:
            continue

        if day < 1 or day > 31:
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        continue
