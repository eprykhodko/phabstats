import random

from collections import Counter
from operator import itemgetter

from funcy import count_by, cat, filter, pluck, split

from .base import BaseStat


class MostAcceptsRejectsStat(BaseStat):
    title = "Most rigorous reviewers of the week."

    def get_data(self):
        all_transactions = filter(
            lambda t: t["type"] in ("request-changes", "accept"),
            cat(pluck("transactions", self.raw_data)),
        )
        accept_transactions, reject_transactions = split(
            lambda t: t["type"] == "accept", all_transactions
        )
        most_accepting_author, most_accepting_count = Counter(
            count_by(itemgetter("authorPHID"), accept_transactions)
        ).most_common(1)[0]
        most_rejecting_author, most_rejecting_count = Counter(
            count_by(itemgetter("authorPHID"), reject_transactions)
        ).most_common(1)[0]

        return (
            {
                "author": self.users_mapping[most_accepting_author],
                "count": most_accepting_count,
            },
            {
                "author": self.users_mapping[most_rejecting_author],
                "count": most_rejecting_count,
            },
        )

    def get_epithet(self):
        choices = ["an astonishing", "an amazing", "an astounding", "a jaw dropping"]
        return random.choice(choices)

    def get_data_blocks(self):
        accepting, rejecting = self.get_data()
        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'>• {accepting["author"]} has accepted {self.get_epithet()} {accepting["count"]} diffs.\n'
                    f'>• {rejecting["author"]} has rejected {self.get_epithet()} {rejecting["count"]} diffs.',
                },
            }
        ]
