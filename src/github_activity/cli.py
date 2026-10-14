import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Show recent GitHub user activity.")

    parser.add_argument("username", help="GitHub username to fetch activity for")

    args = parser.parse_args()

    print(args.username)


if __name__ == "__main__":
    main()
