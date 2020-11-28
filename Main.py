try:
    from pytube import YouTube, Playlist
    import moviepy.editor as mp
    import os
except Exception as error:
    print(f"{error}:An error ocurred while importing the modules, please restart the program.")
Delist=[]
urList=[]
x1=0
x2=1
Input=""
print("""This is an aplication created by Valentino Amato that downloads videos from youtube
and turns them to mp3 format, great for downloading music!!""")
def Downloader(url):
    download = YouTube(url).streams.filter(subtype='mp4').first().download(os.path.dirname(os.path.realpath(__file__))+r"\Songs")
    mp4_file = str(os.path.dirname(os.path.realpath(__file__))+download.split("YouTube Downloader")[len(download.split("YouTube Downloader"))-1])
    Delist.append(mp4_file)
    mp3file = str(os.path.dirname(os.path.realpath(__file__))+download.split("YouTube Downloader")[len(download.split("YouTube Downloader"))-1])
    mp3_file = mp3file.split(".mp4")[0]+".mp3"
    print(mp3_file)
    videoclip = mp.VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    global x1
    x1+=1
    if x1==len(urList):
        audioclip.close()
        videoclip.close()
        for Song in range(len(Delist)):
            os.remove(Delist[Song])
while x2:
    Input = str(input("""Please enter the links of the videos to download.
Enter "f" when finished:"""))
    if Input!="f":
        urList.append(Input)
    else:
        x2=0
try:
    for i in range(len(urList)):
        Downloader(urList[i])
    print("|"*50)
    print("""All the desire files have been downloaded in the "Songs" folder.
If you want to download more songs please execute the program again.
Thanks for using my app!!.More info in:""")
except Exception as error:
    print(f"{error}:An error ocurred, please restart the program and enter valid links.")






