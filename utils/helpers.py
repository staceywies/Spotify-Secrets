"""
helpers.py
----------
Utility functions for SpotifySecrets project.
Handles formatting, printing, and other reusable helpers.
"""

from typing import List, Dict


def format_track(track: Dict) -> str:
    """
    Format a single track dictionary into a readable string.

    Parameters
    ----------
    track : dict
        A dictionary containing track information:
        - name
        - artists
        - album
        - url

    Returns
    -------
    str
        Formatted string for display.
    """
    return f"🎵 {track['name']} — {track['artists']} ({track['album']})\n   {track['url']}"


def display_top_tracks(tracks: List[Dict]) -> None:
    """
    Nicely prints a list of top tracks.

    Parameters
    ----------
    tracks : list of dict
        List of track dictionaries as returned by fetch_top_tracks.py.
    """
    print("\n🔥 Your Top 5 Spotify Tracks 🔥\n")
    for i, track in enumerate(tracks, start=1):
        print(f"{i}. {format_track(track)}\n")


def extract_track_urls(tracks: List[Dict]) -> List[str]:
    """
    Extract Spotify URLs from a list of track dictionaries.
    Useful for creating playlists or sharing links.

    Parameters
    ----------
    tracks : list of dict
        List of track dictionaries.

    Returns
    -------
    list of str
        List of Spotify track URLs.
    """
    return [track["url"] for track in tracks]
