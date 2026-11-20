# AGENTS.md

## What this is

Mailroom is a command-line tool for one newsletter: Kettlebird Tea's Steep Club.
It reads the subscribers, checks an issue, and sends it to a practice mail server.

## Rules

- **Use uv for everything.** Manage Python, dependencies, and commands with uv
  (`uv add`, `uv sync`, `uv run ...`). Do not use pip, venv, poetry, or a bare `python`.
- **Never use a real person's email address.** Use `@example.com` addresses for
  subscribers and test data, and `@resend.dev` addresses for practice sends.
- **Commit and push after every step.**
- **Behaviors first.** The user gives the expected answers. Write them as checks
  in `checks.py`, run them and show them failing, then write the code that makes
  them pass.
