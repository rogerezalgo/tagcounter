import collections


def count_tags(tags: list[str]):
    """
        Counts tags and returns dictionary which contains
        tag as a key and amount of this as a value
    """

    count = collections.Counter()

    for tag in tags:
        count[tag] += 1

    return dict(count)
