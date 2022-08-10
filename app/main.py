from flask import Flask
from flask_restful import Resource, Api

from api.get_youtube_playlists import GetYoutubePlaylists
from api.create_spotify_playlist import CreateSpotifyPlaylist
from api.generate_spotify_uri import GenerateSpotifyURI
from api.add_song_to_playlist import AddSongToPlaylist
from api.get_songs_from_playlist import GetSongsFromPlaylist


app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('settings.py')

api.add_resource(CreateSpotifyPlaylist, '/createSpotifyPlaylist')
api.add_resource(GetYoutubePlaylists, '/getYoutubePlaylists')
api.add_resource(GenerateSpotifyURI, '/generateSpotifyURI')
api.add_resource(AddSongToPlaylist, '/addSongToPlaylist')
api.add_resource(GetSongsFromPlaylist, '/getSongsFromPlaylist')

if __name__ == '__main__':
    app.run(debug=True)