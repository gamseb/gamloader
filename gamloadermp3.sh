#!/usr/bin/bash
echo "This is a simple youtube downloader"
while true
do
	echo "***********************************"
	echo "Input your url or press ctrl+C to exit"
	read user_input
	youtube-dl --extract-audio --audio-format mp3 --no-check-certificate -o "%(title)s.%(ext)s" $user_input
	echo "Your video has been downloaded"
  # loop infinitely
done
