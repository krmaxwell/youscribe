import youscribe

import pytest
import os


def test_get_yt_code_regular_url():
    # Gangnam Style
    url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
    assert youscribe.get_yt_code(url) == "9bZkp7q19f0"


def test_get_yt_code_blank_url():
    with pytest.raises(ValueError):
        youscribe.get_yt_code("")


def test_get_yt_code_shared_url():
    # Gangnam Style
    url = "https://youtu.be/9bZkp7q19f0?si=nDGUaDzTo5EFiPRN"
    assert youscribe.get_yt_code(url) == "9bZkp7q19f0"


def test_get_yt_code_not_youtube_url():
    with pytest.raises(ValueError):
        youscribe.get_yt_code("https://www.google.com")


@pytest.mark.skip(reason="Network request")
def test_save_url_to_file():
    url = "https://www.youtube.com/watch?v=5La8Ke35drk"
    assert youscribe.save_url_to_file(url) == "5La8Ke35drk.mp4"


def test_get_openai_key_blank():
    with pytest.raises(ValueError):
        youscribe.get_openai_key()


def test_get_openai_key_file():
    assert youscribe.get_openai_key("tests/.openai_test") == "test_key"


def test_get_openai_key_environment():
    os.environ["OPENAI_KEY"] = "test_key"
    assert youscribe.get_openai_key() == "test_key"


def test_get_transcript_for_audio_file_requires_file_name():
    with pytest.raises(ValueError):
        youscribe.get_transcript_for_audio_file("")


def test_get_transcript_for_audio_file_requires_key():
    os.environ["OPENAI_KEY"] = ""
    with pytest.raises(ValueError):
        youscribe.get_transcript_for_audio_file("test.mp4")


@pytest.mark.skip(reason="Network request for expensive API")
def test_get_transcript_for_audio_file_good_file():
    openai_key = youscribe.get_openai_key(".openai")
    youscribe.openai_key = openai_key
    assert len(youscribe.get_transcript_for_audio_file("5La8Ke35drk.mp4")) > 0
