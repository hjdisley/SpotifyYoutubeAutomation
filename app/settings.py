import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CREATE_PLAYLIST_TOKEN = os.getenv('CREATE_PLAYLIST_TOKEN')
ADD_SONG_TO_PLAYLIST_TOKEN = os.getenv('ADD_TO_PLAYLIST_TOKEN')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')
SEARCH_FOR_SONG_TOKEN = os.getenv('SEARCH_FOR_SONG_TOKEN')