from museum.artists import get_artist
from museum.artwork import get_artwork


def main():
    artwork = input("Artwork: ")
    artworks = get_artwork(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

    artist = input("Artwork: ")
    artworks = get_artist(query=artist, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")


if __name__ == "__main__":
    main()
