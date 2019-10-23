import httpx

from phabstats import settings


def send_slack_message(payload):
    headers = {
        'Content-type': 'application/json',
    }
    return httpx.post(settings.SLACK_HOOK_ULR, headers=headers, json=payload)


def send_most_authored_message(most_authored_data):
    payload = {
        'text': 'Your fresh stats!',
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here are the fresh stats"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Most Diffs this week*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": '\n'.join(
                        f'>• {author} with {count} diffs'
                        for author, count in most_authored_data
                    )
                }
            }
        ]
    }
    return send_slack_message(payload)