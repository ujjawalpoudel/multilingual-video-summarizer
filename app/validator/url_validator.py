import pydantic
import regex as re


class URLValidator(pydantic.BaseModel, extra=pydantic.Extra.forbid):
    url: str

    @pydantic.validator("url")
    @classmethod
    def validate_youtube_url(cls, url):
        """
        Validate if the given URL is a valid YouTube URL.

        YouTube URL Pattern:
        (https?://)?(www\.)?                       : Matches optional "http://" or "https://" followed by optional "www."
        (youtube|youtu|youtube-nocookie)\.(com|be)/: Matches one of the three possible domain variations: "youtube.com", "youtu.be", or "youtube-nocookie.com".
        (watch\?v=|embed/|v/|.+\?v=)?              : Matches different URL structures that precede the video ID.
                                                     Allows for variations such as "watch?v=", "embed/", "v/", or a combination of these with additional parameters.
        ([^&=%\?]{11})                             : Matches the video ID, which consists of 11 characters.

        :param url: The URL to validate.
        :return: The validated URL if it is a valid YouTube URL.
        :raises ValueError: If the given URL is not a valid YouTube URL.
        """
        youtube_regex = (
            r"(https?://)?(www\.)?"
            r"(youtube|youtu|youtube-nocookie)\.(com|be)/"
            r"(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
        )
        match = re.match(youtube_regex, url)
        if match is not None:
            return url
        else:
            message = f"The provided URL '{url}' is not a valid YouTube URL."
            raise ValueError(message)
