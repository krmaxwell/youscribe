import pytest
from youscribe import get_yt_code


def test_get_yt_code_regular_url():
    # Gangnam Style
    url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
    assert get_yt_code(url) == "9bZkp7q19f0"


def test_get_yt_code_blank_url():
    with pytest.raises(ValueError):
        get_yt_code("")


def test_get_yt_code_shared_url():
    # Gangnam Style
    url = "https://youtu.be/9bZkp7q19f0?si=nDGUaDzTo5EFiPRN"
    assert get_yt_code(url) == "9bZkp7q19f0"


def test_get_yt_code_not_youtube_url():
    with pytest.raises(ValueError):
        get_yt_code("https://www.google.com")
