# src/auth.py
from config.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE_STRING
from spotipy.oauth2 import SpotifyOAuth

def authenticate():
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE_STRING
    )

    auth_url = sp_oauth.get_authorize_url()
    print("Open this URL in your browser:", auth_url)

    response = input("Paste the URL you were redirected to:\n")
    token_info = sp_oauth.get_access_token(response)
    print("Access token:", token_info['access_token'])
    return token_info['access_token']

if __name__ == "__main__":
    authenticate()
