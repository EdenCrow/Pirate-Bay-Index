# Pirate Bay Index
In 2012 [TorrentFreak reported on a PirateBay user dumping the entire contents of the website](https://torrentfreak.com/download-a-copy-of-the-pirate-bay-its-only-90-mb-120209/). At the time I made a small Python 3 script as a learning exercise to make it easy to search through this data and start the download in the user's torrenting software. I've uploaded the script here for prosperity, with a small quick change for handling errors with user input in the *download_torrent* function.

## Requirements
- Python 3
- Data dump by allisfine ([download via Dropbox](https://www.dropbox.com/s/19gpiuimeqw7ost/data?dl=0)) (also available via magnet link via the TorrentFreak article)
- A default way of handling magnet links with some sort of torrenting software

## Quick Start
- Download script.py from this repository
- Download the data dump
- Make sure both files are placed in the same folder
- Run the script from the command line
- Follow the instructions to search and download torrents from the dump

## Warnings
- The data included within the dump hasn't been updated since the original release and is not intended to be actually used to download torrents.
- I am also not condoning piracy, this was just a small project I made years ago to help me learn Python.
- While I have attempted to include support for Mac and Linux devices, I have not tested the script on either of these operating systems.
