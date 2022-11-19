from tkinter import *
from pytube import YouTube

# function to download video
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download(r'C:\Users\admin\Downloads')
    video.download()
    Label(root, text='Done! check your download & same folder', font='arial 15').place(x=210, y=210)


root = Tk()
root.geometry('700x300')


root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text='Provide the link of the video you want to download from YouTube', font='arial 15 bold').pack()

# enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=270,y=60)
Entry(root, width=80, textvariable=link).place(x=32, y=90,height=30)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='light green',
           padx=2, command=Downloader).place(x=280, y=155)

root.mainloop()