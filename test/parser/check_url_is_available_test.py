from app.parser.check_url_is_available import check_url_is_available


def test_should_return_true_if_url_is_available():
    assert check_url_is_available('google.com')


def test_should_return_false_if_url_is_unavailable():
    assert not check_url_is_available('google')
