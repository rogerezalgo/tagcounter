import pytest

from app.parser.count_tags import count_tags
from app.parser.get_tags import get_tags

__check_tags = ('html', 'body', 'head')


@pytest.mark.parametrize('tag', __check_tags)
def test_should_return_dict_of_counted_tags(tag: str):
    got_tags = get_tags('google.com')
    counted_tags = count_tags(got_tags)

    assert isinstance(counted_tags, dict)
    # Checking some values in the dict for validity
    assert counted_tags.get(tag) == 1
