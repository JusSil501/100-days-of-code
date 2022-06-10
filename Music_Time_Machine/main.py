from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

response = input("Which year you would like to travel to: Type the date in this format YYYY-MM-DD.")
y = response.split("-")[0]

response_song = requests.get(f"https://www.billboard.com/charts/hot-100/{response}/")

top_100= response_song.text

soup = BeautifulSoup(top_100, "html.parser")


songs = [song.getText().strip() for song in soup.select("li #title-of-a-story")]

redirect_uri ='http://example.com'
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"), client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=redirect_uri, scope=scope, cache_path=".cache"))

user_id = sp.current_user()["id"]

song_uris = []
song = songs[0]

for song in songs:
    result = sp.search(q=f"year:{y}track:{song}", type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} doesnt exist in Spotify. SKipped.")

###creates the playlist

top_songs = sp.user_playlist_create(user=user_id,public=False,name=f"{response} Billboard 100", description= f"A playlist of top 100 songs for year:{response}")


sp.playlist_add_items(playlist_id=top_songs["id"], items=song_uris)


