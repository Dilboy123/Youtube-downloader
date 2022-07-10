# importing packages
from pytube import YouTube
import os


# url input from user
def download_song(link):
    yt = YouTube(link)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    # out_file = video.download(r"C:\Users\dilan\Videos")
    out_file = video.download(r"./mp3")

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.'
    os.rename(out_file, new_file)

    # result of success
    return yt.title
