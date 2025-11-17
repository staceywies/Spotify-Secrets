import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE_STRING
from utils.helpers import format_tracks

def get_top_tracks(limit=5):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE_STRING
    ))

    top_tracks = sp.current_user_top_tracks(limit=limit)
    formatted = format_tracks(top_tracks['items'])
    for track in formatted:
        print(track)

if __name__ == "__main__":
    get_top_tracks()
