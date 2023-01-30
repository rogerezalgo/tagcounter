import requests as req
from bs4 import BeautifulSoup

from .check_url_is_available import check_url_is_available
from .normalize_url import normalize_url


def get_tags(url: str):
    """
        Parses url from parameter and returns a list of tags
    """

    is_url_valid = check_url_is_available(url)

    if not is_url_valid:
        raise ValueError('Can not parse the url')

    resp = req.get(normalize_url(url))
    soup = BeautifulSoup(resp.text, 'html.parser')

    return [(lambda tag: tag.name)(tag) for tag in soup.recursiveChildGenerator() if tag.name]
