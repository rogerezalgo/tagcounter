import requests

from .normalize_url import normalize_url


def check_url_is_available(url: str):
    """
        Checks for url availability
    """

    valid_url: str = normalize_url(url)

    try:
        requests.get(valid_url)
    except:
        return False
    else:
        return True
