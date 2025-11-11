"""
fetch_top_tracks.py
-------------------
Fetches a user's top 5 tracks from Spotify using the Web API.

Requires a valid access token with the `user-top-read` scope.
You can obtain one via the OAuth flow implemented in auth.py.
"""

import requests


def get_top_tracks(access_token: str, limit: int = 5, time_range: str = "long_term"):
    """
    Retrieve the user's top tracks from Spotify.

    Parameters
    ----------
    access_token : str
        A valid Spotify OAuth access token with `user-top-read` scope.
    limit : int, optional
        Number of tracks to return (default is 5).
    time_range : str, optional
        Time range for top tracks. Options:
        - 'short_term' (last 4 weeks)
        - 'medium_term' (last 6 months)
        - 'long_term' (all time)

    Returns
    -------
    list[dict]
        A list of dictionaries with track name, artists, album, and URL.
    """
    url = "https://api.spotify.com/v1/me/top/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"limit": limit, "time_range": time_range}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            f"Spotify API error {response.status_code}: {response.json().get('error', {}).get('message', '')}"
        )

    data = response.json().get("items", [])
    tracks = [
        {
            "name": track["name"],
            "artists": ", ".join([artist["name"] for artist in track["artists"]]),
            "album": track["album"]["name"],
            "url": track["external_urls"]["spotify"],
        }
        for track in data
    ]

    return tracks


if __name__ == "__main__":
    # Example usage (replace with your access token for local testing)
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
    try:
        top_tracks = get_top_tracks(ACCESS_TOKEN)
        print("\n🎵 Your Top 5 Spotify Tracks 🎵\n")
        for i, track in enumerate(top_tracks, start=1):
            print(f"{i}. {track['name']} — {track['artists']} ({track['album']})")
            print(f"   {track['url']}\n")
    except Exception as e:
        print("Error:", e)
