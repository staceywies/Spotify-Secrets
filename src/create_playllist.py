"""
create_playlist.py
------------------
Creates a Spotify playlist and adds a list of track URLs to it.

Requires:
- A valid access token with playlist-modify-public or playlist-modify-private scopes.
- The user's Spotify ID (retrieved via the Web API or passed manually).

This module is optional but demonstrates full API workflow integration.
"""

import requests
from typing import List


def get_current_user_id(access_token: str) -> str:
    """
    Fetch the current user's Spotify ID.

    Parameters
    ----------
    access_token : str
        Valid OAuth access token.

    Returns
    -------
    str
        The user's Spotify ID.
    """
    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to get current user: {response.text}")

    return response.json().get("id")


def create_playlist(access_token: str, user_id: str, name: str, description: str = "") -> str:
    """
    Create a Spotify playlist for the user.

    Parameters
    ----------
    access_token : str
        Valid OAuth access token.
    user_id : str
        Spotify user ID.
    name : str
        Playlist name.
    description : str, optional
        Playlist description.

    Returns
    -------
    str
        The new playlist's Spotify ID.
    """
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json"}

    data = {
        "name": name,
        "description": description,
        "public": True
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code not in (200, 201):
        raise Exception(f"Failed to create playlist: {response.text}")

    return response.json().get("id")


def add_tracks_to_playlist(access_token: str, playlist_id: str, track_urls: List[str]) -> None:
    """
    Add tracks to a given playlist.

    Parameters
    ----------
    access_token : str
        Valid OAuth access token.
    playlist_id : str
        ID of the playlist to modify.
    track_urls : list of str
        Spotify track URLs to add.

    Returns
    -------
    None
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json"}

    data = {"uris": track_urls}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code not in (200, 201):
        raise Exception(f"Failed to add tracks: {response.text}")


if __name__ == "__main__":
    # Example usage
    ACCESS_TOKEN = input("Enter your OAuth access token:\n> ").strip()

    try:
        user_id = get_current_user_id(ACCESS_TOKEN)
        print(f"👤 Logged in as Spotify user: {user_id}")

        playlist_id = create_playlist(
            access_token=ACCESS_TOKEN,
            user_id=user_id,
            name="My Top 5 Tracks",
            description="Automatically generated playlist of my top songs."
        )
        print(f"🎶 Playlist created! ID: {playlist_id}")

        urls = [
            # Example:
            # "spotify:track:123...",
        ]
        add_tracks_to_playlist(ACCESS_TOKEN, playlist_id, urls)
        print("✅ Tracks added to your playlist!")

    except Exception as e:
        print("Error:", e)
