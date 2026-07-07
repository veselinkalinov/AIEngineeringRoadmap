def main():
    time = input("What time is it? ")
    sum_time = convert(time)

    if sum_time >= 7 and sum_time <= 8:
        print("breakfast time")
    elif sum_time >= 12 and sum_time <= 13:
        print("lunch time")
    elif sum_time >= 18 and sum_time <= 19:
        print("dinner time")


def convert(time: str) -> int:
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    float_mins = round(minutes/60, 2)
    sum_time = hours + float_mins

    return sum_time


if __name__ == "__main__":
    main()
