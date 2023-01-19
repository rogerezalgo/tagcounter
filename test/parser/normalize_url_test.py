import pytest

from app.parser.normalize_url import normalize_url

__urls = ('google.com', 'https://google.com', 'www.google.com', 'https://www.google.com')


@pytest.mark.parametrize('url', __urls)
def test_normalize_url(url: str):
    normalized_url: str = normalize_url(url)

    assert normalized_url == 'https://www.google.com'


def test_should_raise_exception_if_empty_url():
    with pytest.raises(TypeError):
        normalize_url('')
