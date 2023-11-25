from urllib.parse import urlparse


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
