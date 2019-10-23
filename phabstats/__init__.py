from .phab.data import get_raw_data, get_users_mapping
from .phab.processors import most_authored
from .slack import send_most_authored_message


def main():
    raw_data = get_raw_data()
    most_authored_data = most_authored(raw_data, get_users_mapping())
    send_most_authored_message(most_authored_data)

