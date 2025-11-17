"""
config.py
---------
Loads environment variables for Spotify API credentials.
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Spotify API credentials
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Scopes your app will request
SCOPES = [
    "user-top-read",            # Read user's top tracks
    "playlist-modify-public",   # Optional: create public playlists
    "playlist-modify-private"   # Optional: create private playlists
]

# Optional: convert scopes list to space-separated string (needed for Spotipy)
SCOPE_STRING = " ".join(SCOPES)

# Sanity check: warn if any credential is missing
if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
    raise EnvironmentError(
        "Spotify credentials not set in .env. "
        "Make sure SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI exist."
    )
