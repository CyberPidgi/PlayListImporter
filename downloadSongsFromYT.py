from Song import Song
from typing import List
from youtube_dl import YoutubeDL
from findSongYtLink import get_links_for
import asyncio

ytdl_format_options = {
    'format': 'm4a',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ytdl = YoutubeDL(ytdl_format_options)


def download_all(songs: List[Song]):
    links = asyncio.run(get_links_for(songs))

    for song, link in zip(songs, links):
        download(song, link)


def download(song: Song, link: str):
    """

    :param song: an instance of Song
    :param link: a Youtube video link
    """
    print()
    print(f"Downloading {song.name} by {song.artist}")
    data: List[dict] = ytdl.extract_info(url=link, download=True)
    print(data)
    print(f"Downloaded {song.name} by {song.artist}!")


if __name__ == '__main__':
    download_all([Song('Heather', 'Conan Gray')])
