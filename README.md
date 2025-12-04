# MusicAnalytics
A lightweight Python tool for analyzing personal Spotify listening habits.

MusicAnalytics is a small project that uses the Spotify Web API to fetch your top tracks over different time ranges.

1️⃣ Create a Spotify Developer App

Go to https://developer.spotify.com/dashboard

Create a new app

Add a redirect URI:

http://127.0.0.1:8888/callback


Copy your Client ID and Client Secret

2️⃣ Add Them to .env

Create a .env file in your project root with:

SPOTIFY_CLIENT_ID=your_id_here
SPOTIFY_CLIENT_SECRET=your_secret_here
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback

# Optional settings
SPOTIFY_TIMEFRAME=long_term
SPOTIFY_LIMIT=5

3️⃣ Install Dependencies
pip install spotipy python-dotenv

4️⃣ Authenticate

Run:

python src/auth.py


This will:

Open a browser window

Let you log into Spotify

Save your token in .cache (auto-ignored)

🎵 Fetch Your Top Tracks
python src/fetch_top_tracks.py