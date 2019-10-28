from .phab.data import get_raw_data, get_users_mapping
from .slack import send_slack_message
from .stats import MostDiffsStat, MostAcceptsRejectsStat


class StatsComposer:

    stats = (MostDiffsStat, MostAcceptsRejectsStat)

    def __init__(self, raw_data, users_mapping):
        self.raw_data = raw_data
        self.users_mapping = users_mapping

    def get_all_blocks(self):
        blocks = []
        for stat_cls in self.stats:
            stat = stat_cls(self.raw_data, self.users_mapping)
            blocks.extend(stat.get_blocks())
        return blocks

    def make_slack_message_payload(self):
        blocks = self.get_all_blocks()
        return {
            "text": "Your fresh stats!",
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Here are the fresh stats"},
                },
                *blocks,
            ],
        }


def main():
    composer = StatsComposer(get_raw_data(), get_users_mapping())
    payload = composer.make_slack_message_payload()
    send_slack_message(payload)
