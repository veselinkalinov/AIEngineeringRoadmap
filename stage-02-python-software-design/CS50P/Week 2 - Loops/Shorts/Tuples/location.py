import sys


def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]

    latitude, longitude = coordinates_tuple
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    """Tuples don't support item assignment (changing items in the tuple). Tuples are better for memory, data"""

    print(f"Tuple is {sys.getsizeof(coordinates_tuple)} bytes")
    print(f"List is {sys.getsizeof(coordinates_list)} bytes")


if "__main__" == __name__:
    main()
