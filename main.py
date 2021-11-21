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
        os.chdir(i.channel_name)
        videosneu = i.videos
        for x in videosneu:
            videotitel.append(x.title)  # bis hier funkt
        # print(videotitel)
        videosda = [os.path.splitext(filename)[0] for filename in os.listdir()]
        # print(videosda)

        aa = set(videotitel)
        bb = set(videosda)
        cc = aa - bb
        print(cc)
        os.chdir("..")

# videotitel als dictionary gemeinsam mit den urls


    # for x in i.videos:
    #    print(i.videos.title)
   # os.chdir("..")

    print(os.listdir())  # hier zweite for-schleife ansetzen
    os.chdir("..")

# for b in yt_objects:
#     latest.append(YouTube(b[0]))
#
# for c in latest:
#     print(c.title)
#


# if "neuestes video" in videoordner:
#     download video
# else:
#     do nothing
#

#2



from pathlib import Path




yt2 = YouTube(channels[0])

yt = YouTube('https://www.youtube.com/user/BBC/videos')
zz = Channel('https://www.youtube.com/user/BBC/videos')

x = yt.streams
y = yt.streams.filter(file_extension="mp4")
z = y.get_highest_resolution()
video.streams.get_by_itag(18).download()
z.download(output_path="/home/ingvio/")

for url in x.video_urls:
    print(url)


z = yt_objects[0].videos
for i in z: # gibt die titel aus
    print(i.title)

yt = YouTube('https://www.youtube.com/watch?v=4Ey0SceXcx8')
yt1 = yt.streams.get_highest_resolution()
yt1.download(filename=yt.title) # er verschluckt sonst  das komma


xxx = aa - bb # funktioniert nicht...

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
    #print(kombi)
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

# gibt das eine rausgefilterte video an, das schon auf der platte ist
for k in kombi:
    if k  in bb:
        print(kombi[k])

    # entwurf: if k not in "videosda":
    # pass kombi[k] to download.


