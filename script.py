import os
import platform
import sys
import time
import subprocess

# Key:
# A = TBP ID
# B = TorrentName
# C = Size In Bytes
# D = Seeders5
# E = Leechers
# F = MagnetLinkHash

# Download A Torrent Via Magnet Link
def download_torrent(torrentmagnet, results):
	# Prepare Correct Magnet Link
	if results > 1:
		true_number = False
		while not true_number:
			usr_input = ''
			while type(usr_input) != int:
				 usr_input = input("Download Torrent Number: ")
				 try:
				 	usr_input = int(usr_input)
				 except ValueError:
				 	print("Input is not a valid number")
			if 0 < int(usr_input) <= results:
				true_number = True
				torrent_number = usr_input
			else:
				print("Number is not in results range (1 - " + str(results) + ")")
		magnet_link = torrentmagnet[torrent_number-1]
	elif results == 1:
		magnet_link = magnet_link = torrentmagnet[0]
	magnet_link = 'magnet:?xt=urn:btih:' + magnet_link
	# Start The Default Program For Handling Magnet Links
	operating_system = platform.system()
	operating_system = operating_system.lower()
	# Windows
	if ('windows' in operating_system) | ('win32' in operating_system) | ('win64' in operating_system):
		try:
			os.startfile(magnet_link)
			print("Download Initiated")
		except OSError as e:
			print("You do not have a default program for downloading magnet links. Please install one and try again.")
	# Linux
	elif ('linux' in operating_system) | ('linux2' in operating_system):
		try:
			cmd = 'xdg-open ' + magnet_link
			subprocess.call(cmd)
			print("Download Initiated")
		except OSError as e:
			print("You do not have a default program for downloading magnet links. Please install one and try again.")
	# Mac
	elif ('poisx' in operating_system) | ('darwin' in operating_system)| ('mac' in operating_system):
		try:
			cmd = 'osascript -e "tell apllication "Finder" open file, magnet_link, "of desktop"'
			subprocess.call(cmd)
			print("Download Initiated")
		except OSError as e:
			print("You do not have a default program for downloading magnet links. Please install one and try again.")
	# Un-recognised
	else:
		print("Your OS is currently not recognised by this script. Please contact the devloper with the following information:\n", "PLATFORM.SYSTEM() RESULT NOT RECOGNISED: ", operating_system)
		time.sleep(5)
		sys.exit()
	return option_one()

# Search Dump
def search():
	results = 0
	torrentmagnet = []
	searchphrase = input("Search: ")
	with open('data', 'r', encoding="utf8") as inF:
		for line in inF:
			if searchphrase in line:
				a, *b, c, d, e, f = line.strip().split('|')
				b = '|'.join(b)
				results += 1
				print("\n\n", results, "\n", "TPB ID: " + a + "\n", "Torrent: " + b + "\n", "Size (Bytes): " + c + "\n", "Seeders: " + d + "\n", "Leechers: " + e + "\n", "Magnet Hash: " + f + "\n\n")
				torrentmagnet.append(f)
	if results > 0:
		return option_two(torrentmagnet, results)
	else:
		usr_input = ''
		while usr_input not in ['y', 'n']:
			usr_input = input("No torrents found - search again (y/n)?: ").lower()
		if usr_input == 'y':
			search()
		elif usr_input == 'n':
			print("Quitting...")
			time.sleep(2)
			sys.exit()
		
		

# Option One
def option_one():
	usr_input = ''
	while usr_input not in ['1', '2']:
		usr_input = input("Options: '1') Search | '2') Quit\nOption: ")
	if usr_input == '1':
		search()
	elif usr_input == '2':
		sys.exit()

# Option Two
def option_two(torrentmagnet, results):
	usr_input = ''
	while usr_input not in ['1', '2', '3']:
		usr_input = input("Options: '1') Download | '2') Search | '3') Quit\nOption: ")
	if usr_input == '1':
		return download_torrent(torrentmagnet, results)
	elif usr_input == '2':
		return search()
	elif usr_input == '3':
		sys.exit()

# Start Script
print("PirateBay Index - Software by Eden Crow")		
option_one()
