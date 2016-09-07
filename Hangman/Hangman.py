import random
import tkinter
import sys
from PIL import Image,ImageTk

def after_game():
    again = tkinter.Button(window, text='Play again!',command=lambda: new_game())
    again.pack()
    finish = tkinter.Button(window, text='Exit program.',command= lambda: window.destroy())
    finish.pack()

def new_game():
    window.destroy()
    setup()

def set_level(num):
    global lvl
    global wyswietlane_haslo
    global slowo
    lvl = num
    choice1.destroy()
    choice2.destroy()
    choice3.destroy()
    slowo = lines_from_file[(lvl-1)*4+rand]
    wyswietlane_haslo = '_ ' *((2*lvl)+2)
    lbl.configure(text = wyswietlane_haslo, font=('Helvetica',16))
    entry.pack()
    but.pack()
    wprow_lab.pack()

def draw(num):
    img = ImageTk.PhotoImage(Image.open("resources/"+str(num)+".png"))
    glob_label.configure(image=img)
    glob_label.image=img

# main loop: reading entry letter, checking its occurence in solution,
# priting solution, drawing the drawing.

def start():
    global guesses
    global wprow
    global wyswietlane_haslo
    global guessed_letters
    global game_on
    global step_to_death
    global wprow
    
#Read entry and check if it's in solutions string
    
    char = entry.get()
    entry.delete(0)
    guessed_letters = guessed_letters + char
    wprow = wprow + ' ' + str(char)
    wprow_lab.configure(text = wprow)

    wyswietlane_haslo=''
    for letter in slowo:
        if char == letter:
            step_to_death=False
        if char == letter or letter in guessed_letters:
            wyswietlane_haslo = wyswietlane_haslo + letter + ' '
        else:
            if letter != '\n':
                wyswietlane_haslo = wyswietlane_haslo + '_ '
                game_on = True
                
    lbl.configure(text = wyswietlane_haslo)

    if not game_on:
        info.configure(text='***** WYGRAŁEŚ *****\n* URATOWAŁEŚ WIEŚKA *')
        entry.destroy()
        but.destroy()
        after_game()
        
#Draw next step only if user guessed wrong
    if step_to_death:
        guesses+=1

    draw(guesses)

    game_on = False
    step_to_death = True
    
    if(guesses==9):
        info.configure(text='*** PRZEGRAŁEŚ ***\n* WIESIEK ZAWISŁ *')
        entry.destroy()
        but.destroy()
        after_game()

def setup():
    global lvl
    global guesses
    global wyswietlane_haslo
    global slowo
    global guessed_letters
    global game_on
    global step_to_death
    global choice1
    global choice2
    global choice3
    global window
    global lines_from_file
    global rand
    global lbl
    global glob_label
    global but
    global info
    global entry
    global wprow
    global wprow_lab
    
    lvl=0
    guesses=0
    wyswietlane_haslo = ''
    slowo = ''
    guessed_letters=''
    game_on = True
    step_to_death=True

    window = tkinter.Tk()
    choice1 = tkinter.Button(window, text='Łatwy',command=lambda: set_level(1))
    choice2 = tkinter.Button(window, text='Średni',command=lambda: set_level(2))
    choice3 = tkinter.Button(window, text='Trudny',command=lambda: set_level(3))
    window.geometry('500x500')
    window.title('Gra Wisielec')

    pom = tkinter.Label(window, text='')
    pom.pack()

    pom2 = tkinter.Label(window, text='')
    pom2.pack()

    img = ImageTk.PhotoImage(Image.open("resources/0.png"))
    glob_label = tkinter.Label(window, image = img)
    glob_label.pack()

    lbl = tkinter.Label(window, text='Wybierz poziom trudności:\n')
    lbl.pack()

    choice1.pack()
    choice2.pack()
    choice3.pack()

    f=open('Base.txt','r')
    lines_from_file = f.readlines()
    random.seed()
    rand = random.randint(0,3)

    info = tkinter.Label(window, text='\nZgadnij jaka litera znajduje sie w słowie-rozwiązaniu.\nKażda kolejna nietrafiona próba to krok do śmierci wisielca...')
    info.pack()

    entry = tkinter.Entry(window)
    but = tkinter.Button(window, text='Check!',command=lambda: start())
    wprow = 'Sprawdzono: '
    wprow_lab = tkinter.Label(window, text=wprow)

#global variables and starting program
lines_from_file=''
lvl=0
guesses=0
wyswietlane_haslo = ''
slowo = ''
guessed_letters=''
game_on = True
step_to_death=True

setup()

window.mainloop()
