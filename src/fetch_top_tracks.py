import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE_STRING
from utils.helpers import format_track

from dotenv import load_dotenv
load_dotenv()
TIME_RANGE = os.getenv("SPOTIFY_TIMEFRAME", "long_term")  # default to long_term

def get_top_tracks(limit=5, time_range=TIME_RANGE):
    """
    Fetch and print the user's top tracks from Spotify.

    Parameters
    ----------
    limit : int
        Number of top tracks to retrieve (default 5).
    """
    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE_STRING,
        cache_path=".cache"  # optional: saves token for future runs
    ))

    # Fetch top tracks
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)

    # Loop through each track and print formatted string
    print("\nYour Top Tracks:\n")
    for track in top_tracks['items']:
        print(format_track(track))

if __name__ == "__main__":
    get_top_tracks()
