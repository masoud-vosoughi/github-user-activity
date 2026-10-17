import sys
from urllib.error import HTTPError, URLError

import pytest

from github_activity import cli


def test_main_success(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["github-activity", "torvalds"])

    def fake_fetch_events(username):
        assert username == "torvalds"

        return [
            {
                "type": "PushEvent",
                "repo": {"name": "torvalds/linux"},
            }
        ]

    monkeypatch.setattr(cli, "fetch_events", fake_fetch_events)

    exit_code = cli.main()

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "- Pushed to torvalds/linux\n"
    assert captured.err == ""


def test_main_user_not_found(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["github-activity", "missing-user"])

    def fake_fetch_events(username):
        assert username == "missing-user"

        raise HTTPError(
            url="https://api.github.com/users/missing-user/events/public",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )

    monkeypatch.setattr(cli, "fetch_events", fake_fetch_events)

    exit_code = cli.main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "Error: GitHub user not found.\n"


@pytest.mark.parametrize("status_code", [403, 500])
def test_main_other_http_errors(monkeypatch, capsys, status_code):
    monkeypatch.setattr(sys, "argv", ["github-activity", "torvalds"])

    def fake_fetch_events(username):
        assert username == "torvalds"

        raise HTTPError(
            url="https://api.github.com/users/torvalds/events/public",
            code=status_code,
            msg="Simulated HTTP error",
            hdrs=None,
            fp=None,
        )

    monkeypatch.setattr(cli, "fetch_events", fake_fetch_events)

    exit_code = cli.main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == f"Error: GitHub API returned HTTP {status_code}.\n"


def test_main_connection_error(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["github-activity", "torvalds"])

    def fake_fetch_events(username):
        assert username == "torvalds"
        raise URLError("Simulated network outage")

    monkeypatch.setattr(cli, "fetch_events", fake_fetch_events)

    exit_code = cli.main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "Error: Connection failed: Simulated network outage\n"
