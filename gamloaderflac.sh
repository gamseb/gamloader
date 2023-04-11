#!/usr/bin/bash

command=$1

# Allows to use txt files
if [[ "$command" == *.txt ]]; then
    echo "$command"
    command="-a ${command}"
    echo "$command"
fi

yt-dlp -f bestaudio --add-metadata --no-check-certificate --embed-thumbnail --external-downloader aria2c --external-downloader-args '-c -j 3 -x 3 -s 3 -k 1M' --ignore-errors --continue --no-overwrites --split-chapters --download-archive progress.txt --extract-audio --audio-format flac -o "%(title)s.%(ext)s" $command