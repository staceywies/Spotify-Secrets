import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.config import TIME_RANGE

def save_top_tracks(limit=20):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="user-top-read",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri=os.getenv("REDIRECT_URI")
    ))

    results = sp.current_user_top_tracks(limit=limit, time_range=TIME_RANGE)
    
    with open("top_tracks.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Saved top tracks → top_tracks.json")

if __name__ == "__main__":
    save_top_tracks()
