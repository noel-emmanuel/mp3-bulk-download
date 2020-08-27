from pytube import YouTube
import os
from moviepy.editor import *

# link = input("Enter the youtube URL...\n")


# yt = YouTube(link)
# ys = yt.streams.get_highest_resolution()
# print("Downloading... " + yt.title)
# print("Downloaded! to " + path)


print("Reading link in links.txt...")
with open('links.txt') as f:
    alist = [line.rstrip() for line in f]
    for line in alist:
        print(line)

        # for each link in the results file:
        # - download video
        # - convert video to mp3
        # - delete video

        # yt_link = line
        yt = YouTube(line)
        song_name = yt.title
        # terminal output to confirm download has started
        path1 = '/mnt/e/python_mp3'
        print("Starting download for: " + song_name + " and saving to: " + path1)

        # downloading audio only *new change*
        audio_streams = yt.streams.all()
        audio_mp4 = audio_streams[1]
        print(audio_mp4)
        # downloading mp4 audio only file to a path that will be deleted later
        temp_path = audio_mp4.download(path1)   
        mp4_file = temp_path
        print("Converting audio-only video to an mp3 format...")
        # creating a path for audio file to be saved at 
        song_path = path1 + "/" + song_name + ".mp3"
        mp3_file = song_path
        # conversion from mp4 to mp3
        videoclip = VideoFileClip(mp4_file) # create a videoclip object
        audioclip = videoclip.audio # get the audio object from mp4 file
        audioclip.write_audiofile(mp3_file) # save the audio of mp4 into our mp3 path
        audioclip.close()
        videoclip.close()

        os.remove(temp_path)
        print("Finished! Downloaded to " + path1 + "---------------------------")     
