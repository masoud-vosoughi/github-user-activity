import argparse
import sys
from urllib.error import HTTPError, URLError

from github_activity.client import fetch_events


def main() -> int:
    parser = argparse.ArgumentParser(description="Show recent GitHub user activity.")

    parser.add_argument("username", help="GitHub username to fetch activity for")

    args = parser.parse_args()

    try:
        events = fetch_events(args.username)

    except HTTPError as exc:
        if exc.code == 404:
            print("Error: GitHub user not found.", file=sys.stderr)
        else:
            print(f"Error: GitHub API returned HTTP {exc.code}.", file=sys.stderr)
        return 1

    except URLError as exc:
        print(f"Error: Connection failed: {exc.reason}", file=sys.stderr)
        return 1

    print(f"Fetched {len(events)} events.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
