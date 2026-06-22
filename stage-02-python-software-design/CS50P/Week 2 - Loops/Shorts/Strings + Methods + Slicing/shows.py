SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family ",
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.title().strip())

    print(cleaned_shows)
    print("")
    print('\n'.join(cleaned_shows))


if "__main__" == __name__:
    main()
