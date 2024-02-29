import os
from dotenv import load_dotenv
from splitter import split_audio
from song_detection import detect_song
from denoise import reduce_noise
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
playlist_id = os.environ.get("SPOTIFY_PLAYLIST_ID")

# spotify = Spotify(auth_manager=SpotifyOAuth(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri=redirect_uri,
#     scope='playlist-modify-public'))

# from noise_adder import add_noise_to_audio

# add_noise_to_audio("testfile.wav", "raw_files/testfile.wav")

def get_files_in_directory(directory_path):
    try:
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except OSError as e:
        print(f"Error: {e}")
        return []

raw_files = "raw_files"
denoised_files = "denoised_files"
split_files = "split_files"

os.makedirs(raw_files, exist_ok=True)
os.makedirs(denoised_files, exist_ok=True)
os.makedirs(split_files, exist_ok=True)

for file in get_files_in_directory(raw_files):
    reduce_noise(f"{raw_files}/{file}", f"{denoised_files}/{file}")

for file in get_files_in_directory(denoised_files):
    split_audio(f"{denoised_files}/{file}", split_files)

queries = []

for file in get_files_in_directory(split_files):
    query = detect_song(f"{split_files}/{file}")
    print(query)
    queries.append(query)

def search_tracks(query):
    results = spotify.search(q=query, type='track')
    tracks = results['tracks']['items']

    track_ids = [track['uri'] for track in tracks]
    return track_ids

for query in queries:
    track_ids = search_tracks(query)
    print("Found Track IDs:", track_ids)

    if not track_ids:
        print(f"Couldn't find ID for query {query}")
    else:
        track_uris = ['spotify:track:TRACK_ID1', 'spotify:track:TRACK_ID2', ...]
        spotify.playlist_add_items(playlist_id, [track_ids[0]])
