import json
from typing import Any
from urllib.request import Request, urlopen


def fetch_events(username: str) -> list[dict[str, Any]]:
    url = f"https://api.github.com/users/{username}/events/public"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-user-activity",
    }

    request = Request(url, headers=headers)

    with urlopen(request, timeout=10) as response:
        return json.load(response)
