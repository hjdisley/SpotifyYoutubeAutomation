from email import header
from flask import Flask, request
from flask_restful import Resource, Api, current_app as app
import requests

class GenerateSpotifyURI(Resource):
    def __init__(self):
        self.search_token = app.config.get('SEARCH_FOR_SONG_TOKEN')
        self.spotify_user_id = app.config.get('SPOTIFY_USER_ID')

    def get(self, song_name, artist_name):
        try:
            query = "https://api.spotify.com/v1/search?query=track:{}%20artist:{}&type=track&offset=0&limit=1".format(song_name, artist_name)

            headers={
                "Content-Type":"application/json","Authorization": "Bearer {}".format(self.search_token)
            }

            response = requests.get(query, headers=headers)
            response_json = response.json()

            song = response_json['tracks']['items']
            
            song_uri = song[0]['uri']

            return song_uri
        
        except Exception as e:
            print(e)
            return 'Song not found'

