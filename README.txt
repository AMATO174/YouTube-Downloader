This program created by Valentino Amato lets download videos from youtube
and turns them to MP3 format, great for downloading music!!
Instructions:
1-Create a folder named "Songs" in the same folder as the main script.
2-Run the main script.
3-Enter all the desire YouTube links and then enter "f".
4-Done. All the songs will be found in the "Songs" folder.
Detailled Working:
1-The user enters the links.
2-The links are stored in a list.
3-The links are downloaded one by one by the pytube library as MP4 files. 
4-Since we want MP3 files, we convert them with moviepy library
5-Finally we delete the MP4 files. 
Note:
The files could be configurated like this:

YouTube Downloader(Folder)---------->Main.py(Main program)
				|
				|__>Songs(Folder)_____>DownloadedSongs.mp3(mp3 file)
				

The name of the program(Main.py) isn't critic, but the name of the two folders is very important, the main folder
has to be named as "YouTube Downloader", and the second folder (where the songs will be allocated) has to be named "Songs"	
More info at: https://github.com/AMATO174/YouTube-Downloader				