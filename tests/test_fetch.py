import pytest
from youscribe import get_yt_code, save_url_to_file, get_transcript_for_file


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


@pytest.mark.skip(reason="Network request")
def test_save_url_to_file():
    url = "https://www.youtube.com/watch?v=5La8Ke35drk"
    assert save_url_to_file(url) == "5La8Ke35drk.mp4"


def test_get_transcript_for_file():
    file_name = "5La8Ke35drk.mp4"
    assert get_transcript_for_file(file_name) == "Hello, world!"
