import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)

    if match is None:
        return False

    for number in match.groups():
        if len(number) > 1 and number.startswith("0"):
            return False

        if not 0 <= int(number) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
