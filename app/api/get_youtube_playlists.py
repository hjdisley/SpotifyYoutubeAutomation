from  flask import Flask, request
from flask_restful import Resource, Api, current_app as app
from utils import get_youtube_client

class GetYoutubePlaylists(Resource):
    def __init__(self):
        self.youtube_client = get_youtube_client(app.config.get('YOUTUBE_API_KEY'))
        self.channel_id = request.args.get('channel_id')

    def get(self):
        try:

            request = self.youtube_client.playlists().list(
            part='snippet,contentDetails',
            channelId=self.channel_id,
            )

            response = request.execute()

            playlists=[]

            for playlist in response['items']:
                playlists.append({playlist['snippet']['title']:playlist['id']})

            return {'channel_id': self.channel_id,'playlists':playlists}, 200
        
        except Exception as e:
            print('Error => {}'.format(e))
            return {'message': 'Something went wrong'}, 500