from flask import Flask, request
from flask_restful import Resource, Api, current_app as app
from utils import get_youtube_client
from api.generate_spotify_uri import GenerateSpotifyURI
import youtube_dl

class GetSongsFromPlaylist(Resource):
    def __init__(self):
        self.youtube_client = get_youtube_client(app.config.get('YOUTUBE_API_KEY'))
        self.playlist_ids = request.args.get('playlist_ids').split(',')

    def get(self):
        try:    
            for playlist in self.playlist_ids:  
                request = self.youtube_client.playlistItems().list(
                    part='snippet',
                    playlistId=playlist,
                    prettyPrint=True
                )

                response = request.execute()

                songs=[]

                for song in response['items']:
                    video_id = song['snippet']['resourceId']['videoId']

                    youtube_url = 'https://www.youtube.com/watch?v=' + video_id

                    youtube_info = youtube_dl.YoutubeDL({}).extract_info(
                        youtube_url,
                        download=False
                    )

                   
                    artist = youtube_info['title'].split(' - ')[0]
                    song_name = youtube_info['title'].split(' - ')[1]

                    if artist and song_name is not None:
                        songs.append({
                            'youtube_url': youtube_url,
                            'title': song_name,
                            'artist': artist,
                            'spotify_uri': GenerateSpotifyURI().get(song_name, artist)
                        })


                return songs, 200
    
        except Exception as e:
            print('Error => {}'.format(e))
            return {'message': 'Something went wrong'}, 500