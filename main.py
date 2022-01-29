from getSongsFromPlaylist import get_songs_from_playlist
from downloadSongsFromYT import download_all


def main():
    print("Getting your desired playlist's link ...")
    songs = get_songs_from_playlist(playlist_name='EPIC')
    print("Got the link!")
    print()
    print("Downloading the playlist ...")
    download_all(songs)
    print("Downloaded!")


if __name__ == '__main__':
    main()
