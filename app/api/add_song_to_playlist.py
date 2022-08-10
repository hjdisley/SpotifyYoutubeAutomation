from flask import Flask
from flask_restful import Resource, Api, current_app as app
from utils import get_youtube_client

class AddSongToPlaylist(Resource):
    def __init__(self):
        self.youtube_client = get_youtube_client(app.config('YOUTUBE_API_KEY'))

    def get(self, playlist_id):
        return {'message': 'Add Song To Playlist'}