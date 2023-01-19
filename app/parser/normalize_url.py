def normalize_url(url: str):
    """
        Normalizes url and becomes it to "https://www.url.domen" format
    """

    protocol = 'https://'
    triple_w = 'www.'

    if not url:
        raise TypeError('Empty URL')
    elif protocol in url and triple_w in url:
        return url
    elif protocol in url and triple_w not in url:
        address: str = url[url.find("/") + 2:]
        return f'{protocol}{triple_w}{address}'
    elif protocol not in url and triple_w in url:
        return f'{protocol}{url}'
    else:
        return f'{protocol}{triple_w}{url}'
