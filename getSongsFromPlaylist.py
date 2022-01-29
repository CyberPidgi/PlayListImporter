import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Song import Song
from typing import List

scope = 'user-library-read'
CLIENT_ID = "4abb2bb4108e4bfeb9eb55f46deb4af3"
CLIENT_SECRET = "60a881d9384b46b5a3ea7a4bf42f2cf6"
REDIRECT_URI = 'https://example.com/callback'


def get_songs_from_playlist(playlist_name: str, username: str = None) -> List[Song]:
    """
    :param playlist_name: the name of the playlist (case sensitive)
    :param username: the name of the account. None, if you are running it for yourself.
    :return: the playlist url
    """

    print("Starting Authorization ...")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   scope=scope,
                                                   username=username,
                                                   redirect_uri=REDIRECT_URI))
    print("Done Authorizing!")

    playlists = {item['name']: item['id'] for item in sp.current_user_playlists()['items']}
    playlist_id = playlists[playlist_name]    
    songs = [Song(name=item['track']['name'], artist=item['track']['artists'][0]['name'])
             for item in sp.playlist_items(playlist_id)['items']]
    return songs
        

if __name__ == '__main__':
    get_songs_from_playlist('Sad Vibes', '8skulovxitbpca2cx35h4o81c')
