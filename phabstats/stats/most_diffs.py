from collections import Counter

from funcy import partial, count_by, get_in

from .base import BaseStat


class MostDiffsStat(BaseStat):
    title = "Most Diffs this week"

    def get_data(self):
        counts = Counter(
            count_by(partial(get_in, path=["fields", "authorPHID"]), self.raw_data)
        ).most_common(3)
        return [(self.users_mapping[author], count) for author, count in counts]

    def get_data_blocks(self):
        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "\n".join(
                        f">• {author} with {count} diffs"
                        for author, count in self.get_data()
                    ),
                },
            }
        ]
