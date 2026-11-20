"""Mailroom: the command-line tool for Kettlebird Tea's Steep Club newsletter.

Usage:
    uv run mailroom.py subscribers
"""

import argparse
import csv
from collections import Counter

SUBSCRIBERS = "data/subscribers.csv"


def read_subscribers(path: str) -> list[dict[str, str]]:
    """Return one dict per subscriber row in the CSV file."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_subscribers(path: str) -> int:
    """Return the total number of subscribers."""
    return len(read_subscribers(path))


def count_by_group(path: str) -> dict[str, int]:
    """Return how many subscribers are in each group, sorted by group name."""
    counts = Counter(row["group"] for row in read_subscribers(path))
    return dict(sorted(counts.items()))


def show_subscribers(path: str) -> None:
    """Print the total, then one line per group."""
    print(f"Total: {count_subscribers(path)}")
    for group, count in count_by_group(path).items():
        print(f"{group}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="mailroom", description="Mailroom for the Steep Club newsletter."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("subscribers", help="count the subscribers, in total and by group")
    args = parser.parse_args()

    if args.command == "subscribers":
        show_subscribers(SUBSCRIBERS)


if __name__ == "__main__":
    main()
