import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import dotenv_values
import pprint


secrets = dotenv_values("secrets.env")
scopes = [
    "user-read-currently-playing",
    "user-modify-playback-state",
    ]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=secrets["SPOTIFY_CLIENT_ID"],
        client_secret=secrets["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=secrets["SPOTIFY_REDIRECT_URI"],
        scope=scopes))


results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

print(sp.current_user_playing_track())


sp.add_to_queue(results["tracks"]["items"][0]["id"])

