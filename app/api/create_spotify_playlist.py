from flask import Flask, Response
from flask_restful import Resource, Api, current_app as app
import json
import requests

class CreateSpotifyPlaylist(Resource):
    def __init__(self):
        self.token = app.config.get('CREATE_PLAYLIST_TOKEN')
        self.spotify_user_id = app.config.get('SPOTIFY_USER_ID')

    def get(self):
        try:
            request_body = json.dumps({
                "name": "test playlist",
                "description": "testing playlist",
                "public": True
            })

            query = "https://api.spotify.com/v1/users/{}/playlists".format(self.spotify_user_id)

            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.token)
            }

            response = requests.post(query, data=request_body, headers=headers)

            response_json = response.json()
            
            return {"created_playlist_id":response_json['id']}, 201
        
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500