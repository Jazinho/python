import tkinter
import os
from pygame import mixer
from PIL import Image,ImageTk

possibilities = {'Holly Dolly':['Polka Song','Kanikuly','Merci','Holly Dolly'],
                 'Billie Jean':['Thriller', 'Billie Jean', 'Come On', 'Infinity'],
                 'Scenariusz Dla Moich Sasiadow':['Scenariusz Dla Moich Sasiadow', 'Serce Me', 'Historia Jednej Znajomosci', 'Czerwona Sukienka'],
                 'Beds Are Burning':['Friend in Deed' ,'Sour Love','Beds Are Burning', 'Dark Time'],
                 'We Built This City':['Geronimo\'s Cadillac','War Machine','Brother Louie' ,'We Built This City'],
                 'Espanol':['Espanol', 'Papa\'s Got a New Pigbag', 'El Mismo Sol', 'Bailar'],
                 'Hit That':['Thunderstruck','Hit That', 'Defy You', 'What Happened to You'],
                 'Perry Manson Theme':['Pixelated', 'Think', 'Perry Manson Theme', 'Inspector Harry'],
                 'Pixelated':['Still with You', 'Stay with Me Babe','Mama Said','Pixelated'],
                 'Propaganda':['Big Baton', 'Luźny Łan', 'Burza w Porcie Winczeston','Propaganda'],
                 'Roll With It':['Roll With It', 'Little by Little', 'Stand by Me','Story of me']
                }

def show_buttons(played_song):
    global possibilities
    global ans0
    global ans1
    global ans2
    global ans3
    
    ans0 = tkinter.Button(window, text=possibilities[played_song][0], command= lambda: check(played_song, possibilities[played_song][0]))
    ans1 = tkinter.Button(window, text=possibilities[played_song][1], command= lambda: check(played_song, possibilities[played_song][1]))
    ans2 = tkinter.Button(window, text=possibilities[played_song][2], command= lambda: check(played_song, possibilities[played_song][2]))
    ans3 = tkinter.Button(window, text=possibilities[played_song][3], command= lambda: check(played_song, possibilities[played_song][3]))
    ans0.pack()
    ans1.pack()
    ans2.pack()
    ans3.pack()

def check(correct_ans, tried_title):
    global played_song
    global points
    global cur_song

    mixer.music.pause()
    
    if tried_title == correct_ans:
        points=points+1
        points_lab.configure(text="Points:\n"+str(points)+"\n")

    ans0.destroy()
    ans1.destroy()
    ans2.destroy()
    ans3.destroy()

    cur_song = cur_song+1

    if cur_song < len(songs_list):
        play_song(songs_list[cur_song])
    else:
        points_lab.config(text="Game ended.\nYou got "+str(points)+" points!")

def play_song(filename):
    mixer.music.load('probes/easy/'+filename+'.mp3')
    mixer.music.play()
    show_buttons(os.path.splitext(filename)[0])
    

points = 0
cur_song = 0
songs_list = []

window = tkinter.Tk()
window.title('Music Quiz - check your music knowledge!')
window.geometry('500x400')

img = ImageTk.PhotoImage(Image.open("Theme.png"))
panel = tkinter.Label(window, image = img)
panel.pack()

info_lab = tkinter.Label(window, text = "Guess the title of the song you hear:\n\n")
info_lab.pack()

points_lab = tkinter.Label(window, text = "Points:\n"+str(points)+"\n")
points_lab.pack()

mixer.init()

for filename in os.listdir('./probes/easy'):
    songs_list = songs_list+[os.path.splitext(filename)[0]]

play_song(songs_list[0])

window.mainloop()

