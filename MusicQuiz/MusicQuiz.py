#!C:\Python34\python.exe

import tkinter
import os
import pygame
from pygame import *
from PIL import Image,ImageTk
from Question import *
from Possibilities import possibilities
import time            

def replay_song(question):
    mixer.music.load('resources/'+question.level+question.title+'.mp3')
    mixer.music.play()

def update():
    global label,photo,i,window

    if(i==19):
        return
    photo = tkinter.PhotoImage(file = 'resources/10sec_loading_bar.gif', format="gif -index "+str(i))
    label.configure(image = photo)
    i=i+1
    window.after(500,update)
    
def end_song():
    mixer.music.pause()
    
def play_song(question):
    window.after(500, update)
	
    if question.level == "easy/":
        level_tab.configure(text = "Level: Easy\n")
    else:
        level_tab.configure(text = "Level: Hard\n")
    mixer.music.load(Question.path + question.level + question.title + '.mp3')
    mixer.music.play()
    window.after(10000, end_song)
    retry_but.configure(command = lambda: replay_song(question))
    show_buttons(question.title)
    
def show_buttons(played_song):
    global ans0
    global ans1
    global ans2
    global ans3
    
    ans0 = tkinter.Button(window, text = possibilities[played_song][0], command = lambda: check(played_song, possibilities[played_song][0]))
    ans1 = tkinter.Button(window, text = possibilities[played_song][1], command = lambda: check(played_song, possibilities[played_song][1]))
    ans2 = tkinter.Button(window, text = possibilities[played_song][2], command = lambda: check(played_song, possibilities[played_song][2]))
    ans3 = tkinter.Button(window, text = possibilities[played_song][3], command = lambda: check(played_song, possibilities[played_song][3]))
    ans0.pack()
    ans1.pack()
    ans2.pack()
    ans3.pack()

def check(correct_ans, tried_title):
    global played_song
    global points
    global cur_song
    global i

    end_song()
    
    if tried_title == correct_ans:
        points=points+1

    ans0.destroy()
    ans1.destroy()
    ans2.destroy()
    ans3.destroy()

    i=1
    photo = tkinter.PhotoImage(file = 'resources/10sec_loading_bar.gif', format="gif -index "+str(i))
    label.configure(image = photo)

    cur_song = cur_song+1

    if cur_song < len(questions):
        play_song(questions[cur_song])
        points_lab.configure(text = "\nPoints:\n" + str(points) + "/" + str(cur_song) + "\n")
    else:
        retry_but.destroy()
        info_lab.destroy()
        level_tab.destroy()
        points_lab.config(text="Game ended.\nYou got "+str(points) + "/" + str(cur_song) + " points!", font=("Helvetica", 26))

#mainloop

questions = []

for filename in os.listdir('./resources/easy'):
    title = os.path.splitext(filename)[0]
    questions = questions + [Question("easy/", title, possibilities[title])]

for filename in os.listdir('./resources/not_so_easy'):
    title = os.path.splitext(filename)[0]
    questions = questions + [Question("not_so_easy/", title, possibilities[title])]
    
points = 0
cur_song = 0

window = tkinter.Tk()
window.title('Music Quiz - check your music knowledge!')
window.geometry('500x500')

img = ImageTk.PhotoImage(Image.open("resources/Theme.png"))
panel = tkinter.Label(window, image = img)
panel.pack()

info_lab = tkinter.Label(window, text = "Guess the title of the song you hear\n")
info_lab.pack()

level_tab = tkinter.Label(window, text = "\n")
level_tab.pack()

retry_but = tkinter.Button(window, text = 'Replay song')
retry_but.pack()

points_lab = tkinter.Label(window, text = "\nPoints:\n" + str(points) + "/0\n")
points_lab.pack()

photo = tkinter.PhotoImage(file = 'resources/10sec_loading_bar.gif')
label = tkinter.Label(window, image = photo)
label.pack()
i=1

mixer.init()

play_song(questions[0])

window.mainloop()
