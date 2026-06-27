import requests


def get_artist(query: str, limit: int) -> str:
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {
                "q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artist["title"] for artist in content["data"]]
