import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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

    response_url = input("Paste the URL you were redirected to:\n")
    code = sp_oauth.parse_response_code(response_url)
    token_info = sp_oauth.get_access_token(code)
    print("Access token:", token_info['access_token'])
    return token_info['access_token']

if __name__ == "__main__":
    authenticate()
