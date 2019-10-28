class BaseStat:
    title = "Check this out!"

    def __init__(self, raw_data, users_mapping):
        self.raw_data = raw_data
        self.users_mapping = users_mapping

    def get_title_block(self):
        return {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*{self.title}*"},
        }

    def get_data_blocks(self):
        raise NotImplementedError

    def get_blocks(self):
        return [self.get_title_block(), *self.get_data_blocks()]
