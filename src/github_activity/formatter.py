def format_event(event: dict) -> str:
    event_type = event.get("type")

    repo_name = event.get("repo", {}).get("name", "unknown repository")

    action = event.get("payload", {}).get("action")

    if event_type == "PushEvent":
        return f"Pushed to {repo_name}"
    elif event_type == "WatchEvent":
        return f"Starred {repo_name}"
    elif event_type == "IssuesEvent" and action == "opened":
        return f"Opened an issue in {repo_name}"
    elif event_type == "PullRequestEvent" and action == "opened":
        return f"Opened a pull request in {repo_name}"
    else:
        return f"Activity in {repo_name}"
