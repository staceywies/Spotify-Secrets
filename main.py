"""
main.py
-------
Unified entry point for SpotifySecrets.

This script:
1. Fetches your access token from environment variables
2. Retrieves your Top 5 Spotify tracks
3. Displays them using helper functions
"""

import os
from src.fetch_top_tracks import get_top_tracks
from utils.helpers import display_top_tracks


def main():
    access_token = os.getenv("SPOTIFY_ACCESS_TOKEN")

    if not access_token:
        print("⚠️  Please set SPOTIFY_ACCESS_TOKEN in your environment.")
        return

    try:
        tracks = get_top_tracks(access_token)
        display_top_tracks(tracks)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
