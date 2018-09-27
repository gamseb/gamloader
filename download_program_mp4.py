"""A simple program to download youtube videos using youtube-dl"""
import os

print("Hello, This is a simple youtube downloader")
os.system("cd '/home/gamseb/Music/downloads_from_script'")
while True:
    print("*" * 35)
    print("input your url or type \"end\" to exit")
    x = input(" ")
    if x.lower() == "end":
        break
    else:
        os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 " + x)
        print("your video has been downloaded")

