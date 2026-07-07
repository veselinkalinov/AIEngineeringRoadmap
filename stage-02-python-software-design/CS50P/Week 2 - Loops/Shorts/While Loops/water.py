from soil import sample


def main():
    moisture = sample()
    days = 0
    print(f"Day: {days}: Moisture is {moisture} %")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day: {days}: Moisture is {moisture} %")

    print(f"Time to water!. Its day: {days} and moisture is {moisture} %")


if "__main__" == __name__:
    main()
