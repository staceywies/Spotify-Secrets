# src/create_playlist.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE_STRING

def create_playlist(name="My Top Tracks"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE_STRING
    ))

    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False)
    print(f"Playlist created: {playlist['name']} ({playlist['id']})")
    return playlist['id']

if __name__ == "__main__":
    create_playlist()
