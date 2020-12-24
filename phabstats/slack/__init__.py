import httpx

from phabstats import settings


def send_slack_message(payload):
    headers = {"Content-type": "application/json"}
    return httpx.post(settings.SLACK_HOOK_URL, headers=headers, json=payload)
