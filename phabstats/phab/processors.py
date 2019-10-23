from collections import Counter
from funcy import partial, count_by, get_in


def most_authored(raw_data, user_mapping, threshold=3):
    counts = Counter(
        count_by(partial(get_in, path=['fields', 'authorPHID']), raw_data)
    ).most_common(3)
    return [(user_mapping[author], count) for author, count in counts]

