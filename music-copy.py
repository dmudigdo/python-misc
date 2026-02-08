"""
Recursively copies the contents of 'music' into 'music-backup', if the
artist folder title is in the artist.txt file.

Wrote this because I wanted a subset of my music copied into another folder
"""

import shutil
from pathlib import Path

h = Path.home()

dafile = open(h / 'artists.txt', encoding='UTF-8')
artists = (dafile.readlines())

for artist in artists:
    cleanedArtist = artist.strip()
    print (cleanedArtist + ' copied')
    shutil.copytree(h / ('music/' + cleanedArtist), h / ('music-backup/' + cleanedArtist))
