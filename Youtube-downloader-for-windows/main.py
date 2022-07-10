import tkinter as tk
import tkinter.font as font
from mp3 import download_song
from video import Details

BACKGROUND_COLOR = "#2E4053"

root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=900, relief='raised', background=BACKGROUND_COLOR)
canvas1.pack()

label1 = tk.Label(root, text='Zuuli Downloader 🎥', bg=BACKGROUND_COLOR, fg="white")
label1.config(font=('Stencil Std', 35))
canvas1.create_window(400, 35, window=label1)


def click(event):
    url.configure(state=tk.NORMAL)
    url.delete(0, tk.END)
    url.unbind('<Button-1>', clicked)


url = tk.Entry(root)
url.insert(0, 'Enter YouTube URL Here')
canvas1.create_window(400, 140, window=url, height=40, width=700)

clicked = url.bind('<Button-1>', click)


def get_details():
    entry = url.get()
    v1 = Details(entry)
    yt = v1.get_details()

    yt_title = yt.title

    s1 = yt_title[:len(yt_title) // 2]
    print("\n")
    s2 = yt_title[len(yt_title) // 2:]
    new_string = f"{s1} \n {s2}"

    label4 = tk.Label(root, text=f"Title :  {new_string}", font=('helvetica', 20, 'bold'), bg=BACKGROUND_COLOR, fg="white")
    canvas1.create_window(400, 350, window=label4)


def download_video():
    entry = url.get()
    v2 = Details(entry)
    download = v2.download_video()

    s1 = download[:len(download) // 2]
    print("\n")
    s2 = download[len(download) // 2:]
    new_string = f"{s1} \n {s2}"

    label4 = tk.Label(root, text=f"Location: {new_string} has been successfully downloaded.",
                      font=('helvetica', 16, 'bold'),
                      bg=BACKGROUND_COLOR, fg="white")
    canvas1.create_window(400, 400, window=label4)


def download_mp3():
    entry = url.get()
    mp3 = download_song(entry)

    title = mp3.title()

    s1 = title[:len(title) // 2]
    print("\n")
    s2 = title[len(title) // 2:]
    new_string = f"{s1} \n {s2}"

    label4 = tk.Label(root, text=f"{new_string} mp3 has been successfully downloaded.",
                      font=('helvetica', 16, 'bold'),
                      bg=BACKGROUND_COLOR, fg="white")
    canvas1.create_window(400, 400, window=label4)


buttonFont = font.Font(family='Helvetica', size=20)
button1 = tk.Button(text='Get Details', command=get_details, fg='black',
                    font=buttonFont, highlightbackground=BACKGROUND_COLOR)
canvas1.create_window(150, 230, window=button1)

button2 = tk.Button(text='Download Video', command=download_video, fg='black',
                    font=buttonFont, highlightbackground=BACKGROUND_COLOR)
canvas1.create_window(400, 230, window=button2)

button3 = tk.Button(text='Download MP3', command=download_mp3, fg='black',
                    font=buttonFont, highlightbackground=BACKGROUND_COLOR)
canvas1.create_window(650, 230, window=button3)

root.mainloop()
