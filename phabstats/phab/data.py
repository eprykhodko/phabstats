import json
import time

# from tqdm import tqdm
from phabricator import Phabricator
from phabstats import settings


SECONDS_IN_A_WEEK = 604800

phab = Phabricator(host=settings.PHAB_URL, token=settings.PHAB_TOKEN)


def get_revisions(start, end):
    """Get revisions modified between :start: and :end:"""
    response = phab.differential.revision.search(constraints={
        'modifiedStart': start,
        'modifiedEnd': end,
    })
    return response.data


def get_related_transactions(revision_id):
    """Get related transactions.

    Gets all the transactions for specified :revision_id: that happened between
    :start: and :end:
    """
    response = phab.transaction.search(objectIdentifier=f'D{revision_id}')
    return response.data


def get_raw_data():
    now = int(time.time())
    week_before = now - SECONDS_IN_A_WEEK
    revisions = get_revisions(start=week_before, end=now)
    dataset = map(lambda revision: {
        **revision,
        # 'transactions': get_related_transactions(revision['id'])
    }, revisions)
    return list(dataset)


def get_active_users():
    response = phab.user.search(queryKey="active")
    return response.data


def get_users_mapping():
    return {
        item['phid']: f"{item['fields']['realName']} ({item['fields']['username']})"
        for item in get_active_users()
    }


if __name__ == '__main__':
    data = get_raw_data()
    with open('dataset.json', 'w') as f:
        json.dump(data, f, indent=2)