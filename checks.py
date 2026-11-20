"""Expected answers for Mailroom. Run with: uv run python checks.py"""

from mailroom import count_by_group, count_subscribers

SUBSCRIBERS = "data/subscribers.csv"

assert count_subscribers(SUBSCRIBERS) == 24
assert count_by_group(SUBSCRIBERS) == {
    "daily-drinkers": 8,
    "gift-buyers": 8,
    "tea-curious": 8,
}

print("All checks passed.")
