import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


musicplayer = tkr.TK()
musicplayer.title("Music Player")
musicplayer.geometry("450 x 350")

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font ="Helvetica 12 bold", bg="yellow", selectmode = tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()