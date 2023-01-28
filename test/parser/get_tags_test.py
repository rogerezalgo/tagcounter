import pytest

from app.parser.get_tags import get_tags

__check_tags = ('html', 'body', 'head', 'style', 'script')


@pytest.mark.parametrize('tag', __check_tags)
def test_should_return_list_of_tags(tag: str):
    tags: list[str] = get_tags('google.com')

    assert tag in tags
