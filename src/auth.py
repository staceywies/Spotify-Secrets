"""
auth.py
-------
Handles Spotify API authentication using OAuth 2.0.

This module retrieves an access token using your Spotify
Client ID and Client Secret. The token can then be used
to call other Spotify Web API endpoints.

Note: For production, never hardcode credentials. Store
them in environment variables or a config file listed in .gitignore.
"""

import os
import base64
import requests
from urllib.parse import urlencode


def get_auth_url(client_id: str, redirect_uri: str) -> str:
    """
    Generate a Spotify authorization URL for the user to approve access.

    Parameters
    ----------
    client_id : str
        Your Spotify app's client ID.
    redirect_uri : str
        The redirect URI registered with your Spotify app.

    Returns
    -------
    str
        The full authorization URL.
    """
    auth_endpoint = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "user-top-read",
        "show_dialog": "true"
    }
    return f"{auth_endpoint}?{urlencode(params)}"


def get_token(client_id: str, client_secret: str, code: str, redirect_uri: str) -> str:
    """
    Exchange the authorization code for an access token.

    Parameters
    ----------
    client_id : str
        Your Spotify app's client ID.
    client_secret : str
        Your Spotify app's client secret.
    code : str
        The authorization code returned in the redirect.
    redirect_uri : str
        The redirect URI registered with your app.

    Returns
    -------
    str
        The Spotify access token.
    """
    token_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {"Authorization": f"Basic {auth_header}"}

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    }

    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(
            f"Failed to get token: {response.status_code} {response.text}"
        )

    return response.json().get("access_token")


if __name__ == "__main__":
    # Example usage
    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    REDIRECT_URI = "http://localhost:8888/callback"  # example redirect URI

    if not CLIENT_ID or not CLIENT_SECRET:
        print("⚠️  Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in your environment.")
        exit(1)

    print("Visit this URL to authorize access:")
    print(get_auth_url(CLIENT_ID, REDIRECT_URI))

    code = input("\nAfter approving, paste the 'code' parameter from the redirect URL here:\n> ").strip()
    token = get_token(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI)
    print("\n✅ Your access token:\n", token)
