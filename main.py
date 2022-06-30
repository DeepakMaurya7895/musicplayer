from tkinter import*
from pygame import mixer
import os
def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()
def pausesong():
    mixer.music.pause()
def stopsong():
    mixer.music.stop()
def resumesong():
    mixer.music.unpause()
def next_song():
    mixer.music.next()
root=Tk()
root.title("music player")
mixer.init()
playlist=Listbox(root,selectmode=SINGLE,bg="red")
playlist.grid(columnspan=5)
os.chdir('D:\music')
song = os.listdir()
for s in song:
    playlist.insert(END,s)
Button(root,text="play",command=playsong).grid(row=1,column=0)
Button(root,text="pause",command=pausesong).grid(row=1,column=1)
Button(root,text="stop",command=stopsong).grid(row=1,column=2)
Button(root,text="resume",command=resumesong).grid(row=1,column=3)
Button(root,text="next",command=playsong).grid(row=1,column=4)
music.next()
mainloop()