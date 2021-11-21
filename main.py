# pip install pytube
# test

from pytube import YouTube
from pytube import Channel
import os
import pytube
 # direkt ins video verzeichnis wechseln
textfile = open("channels.txt", "r") # Kanäle sollen übergeben werden. Einer pro Zeile.
channels = []    # enthält die Adressen der zu archivierenden Kanäle als String in einer Liste.
yt_objects = []  # enthält das rohe YouTube-Objekt
latest = []
videosda = []
videosneu = []
urlsneu = []



for line in textfile:
    channels.append(line)
textfile.close()
os.chdir("video")


for a in channels:
      yt_objects.append(Channel(a))
  #  counter += 1

for i in yt_objects:
    if i.channel_name not in os.listdir():
        os.mkdir(i.channel_name)

    for i in yt_objects:
        videotitel = []
        videourl = []
        zuladen = []
        os.chdir(i.channel_name)
        videosneu = i.videos
        urlsneu = i.video_urls
        for x in videosneu:
            videotitel.append(x.title)  # bis hier funkt
        # print(videotitel)
        kombi = dict(zip(videotitel, urlsneu))
        # print(kombi)
        videosda = [os.path.splitext(filename)[0] for filename in os.listdir()]
        # print(videosda)

        aa = set(videotitel)
        bb = set(videosda)
        cc = aa - bb
        for k in kombi:
            if k not in bb:
                zuladen.append(kombi[k])
        for z in zuladen:
            # print("lade " + str(len(zuladen)) + " neue videos")
            arg = YouTube(z)
            arg1 = arg.streams.get_highest_resolution()
            arg1.download(filename=arg.title)

        os.chdir("..")