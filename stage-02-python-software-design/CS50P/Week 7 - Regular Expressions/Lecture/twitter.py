import re

url = input("URL: ").strip()

if matches := re.search(
    r"^(?:https?://)?(?:www\.)?twitter\.(?:com|org|uk|bg)/([a-z0-9_]+)",
    url,
    re.IGNORECASE,
):  # "?:" of the beggining makes it so it doesnt capture it as a group
    print(f"Username: {matches.group(1)}")
