"""A simple program to download youtube videos using youtube-dl"""
import subprocess

print("This is a simple youtube downloader")

while True:
    print("*" * 35)
    print("input your url or type \"end\" to exit")
    command = input(" ")
    if command.lower() == "end":
        break
    else:
        subprocess.call("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 -o \"%(playlist_index)s %(title)s.%(ext)s\" " + command, shell=True)
        print("your video has been downloaded")

