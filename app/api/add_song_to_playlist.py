from flask import Flask
from flask_restful import Resource, Api, current_app as app
import json

class AddSongToPlaylist(Resource):
    def __init__(self):
        self.playlist_token = app.config.get('ADD_TO_PLAYLIST_TOKEN')
    
    example_request = 'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    def get(self, playlist_id, songs):
        try:

            request_body = json.dumps({

            })

        
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


    
