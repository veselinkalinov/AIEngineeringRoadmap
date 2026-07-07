def convert(emoticon: str) -> str:
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon


def main():
    emoticon = input()
    emoticon = convert(emoticon)
    print(emoticon)


if __name__ == "__main__":
    main()
