import os
import dotenv

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import isodate

from pprint import pprint
from collections import namedtuple


"""
Example data structure:
    {'etag': 'FEOXYytxsFNwXcIy07iF35xauyQ',
    'items': [{'contentDetails': {'caption': 'false',
                                'contentRating': {},
                                'definition': 'hd',
                                'dimension': '2d',
                                'duration': 'PT2M8S',
                                'licensedContent': True,
                                'projection': 'rectangular'},
                'etag': 'P0UlkuIXpWRERlUT-fQedVbKKXU',
                'id': 'Tn6-PIqc4UM',
                'kind': 'youtube#video',
                'snippet': {'categoryId': '28',
                            'channelId': 'UCsBjURrPoezykLs9EqgamOA',
                            'channelTitle': 'Fireship',
                            'defaultAudioLanguage': 'en',
                            'description': 'React is a little JavaScript library '
                                        'with a big influence over the webdev '
                                        ...
                                        '- Fira Code Font',
                            'liveBroadcastContent': 'none',
                            'localized': {'description': 'React is a little '
                                                        'JavaScript library with '
                                                        ...
                                                        '- Fira Code Font',
                                        'title': 'React in 100 Seconds'},
                            'publishedAt': '2020-09-08T19:06:55Z',
                            'tags': ['webdev',
                                    'app development',
                                    ...
                                    'javascript'],
                            'thumbnails': {'default': {'height': 90,
                                                    'url': 'https://i.ytimg.com/vi/Tn6-PIqc4UM/default.jpg',
                                                    'width': 120},
                                        'high': {'height': 360,
                                                    'url': 'https://i.ytimg.com/vi/Tn6-PIqc4UM/hqdefault.jpg',
                                                    'width': 480},
                                        'maxres': {'height': 720,
                                                    'url': 'https://i.ytimg.com/vi/Tn6-PIqc4UM/maxresdefault.jpg',
                                                    'width': 1280},
                                        'medium': {'height': 180,
                                                    'url': 'https://i.ytimg.com/vi/Tn6-PIqc4UM/mqdefault.jpg',
                                                    'width': 320},
                                        'standard': {'height': 480,
                                                        'url': 'https://i.ytimg.com/vi/Tn6-PIqc4UM/sddefault.jpg',
                                                        'width': 640}},
                            'title': 'React in 100 Seconds'}}],
    'kind': 'youtube#videoListResponse',
    'pageInfo': {'resultsPerPage': 1, 'totalResults': 1}}
 """


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

dotenv.load_dotenv()


def get_build():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    api_key = os.getenv("YOUTUBE_API_KEY")

    # Get credentials and create an API client
    return googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )


def get_video_data(id):
    youtube = get_build()

    request = youtube.videos().list(part="snippet,contentDetails", id=id)
    return parse_data(request.execute())


def parse_data(data):
    return [ItemParser(item).parse() for item in data["items"]]


class ItemParser:
    Filtereditem = namedtuple(
        "Filtereditem",
        "duration channel_title description published_at tags default_thumbnail_url title",
    )

    def __init__(self, item):
        self.item = item

    def parse(self):

        return self.Filtereditem(
            duration=self._duration(),
            channel_title=self._channel_title(),
            description=self._description(),
            published_at=self._published_at(),
            tags=self._tags(),
            default_thumbnail_url=self._default_thumbnail_url(),
            title=self._title(),
        )

    def _duration(self):
        return isodate.parse_duration(
            self.item["contentDetails"]["duration"]
        ).total_seconds()

    def _channel_title(self):
        return self.item["snippet"]["channelTitle"]

    def _description(self):
        return self.item["snippet"]["description"]

    def _published_at(self):
        return self.item["snippet"]["publishedAt"]

    def _tags(self):
        return self.item["snippet"]["tags"]

    def _default_thumbnail_url(self):
        return self.item["snippet"]["thumbnails"]["default"]["url"]

    def _title(self):
        return self.item["snippet"]["title"]
