from app.parser import parse


def test_should_return_dict_of_bytes():
    tags = parse('google.com')

    assert isinstance(tags, bytes)
