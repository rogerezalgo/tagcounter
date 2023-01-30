import json

from .count_tags import count_tags
from .get_tags import get_tags


def parse_and_return_byte_dict(url: str):
    """
        Parses given url and returns a dict in byte representation
    """

    tags_dict: dict[str, int] = count_tags(get_tags(url))

    return json.dumps(tags_dict).encode('utf-8')
