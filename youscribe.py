from urllib.parse import urlparse
from pytube import YouTube


def get_yt_code(url: str):
    if url == "":
        raise ValueError("URL cannot be blank")

    parsed_url = urlparse(url)

    if parsed_url.netloc == "www.youtube.com":
        video_id = parsed_url.query.split("=")[1]
    elif parsed_url.netloc == "youtu.be":
        video_id = parsed_url.path[1:]
    else:
        raise ValueError("URL must be a YouTube URL")
    return video_id


def save_url_to_file(url: str):
    video_id = get_yt_code(url)
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True)[0]
    audio_stream.download(filename=f"{video_id}.mp4")
    return f"{video_id}.mp4"


def get_transcript_for_file(file_name: str):
    return "Hello, world!"
