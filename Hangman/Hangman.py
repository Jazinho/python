import random
import tkinter
import sys

drawing={
        '0':["        ",
             "        ",
             "        ",
             "        ",
             "        ",
             "        ",
             "        ",
             "        "],
        '1':["        ",
             "        ",
             "        ",
             "        ",
             "        ",
             "        ",
             "        ",
             "/ \     "],
        '2':["        ",
             "        ",
             "        ",
             "        ",
             "        ",
             " |      ",
             " |      ",
             "/ \     "],
        '3':["        ",
             "        ",
             "        ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             "/ \     "],
        '4':["        ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             "/ \     "],
        '5':["  ___   ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             "/ \     "],
        '6':["  ___   ",
             " |   |  ",
             "  |  O  ",
             " |      ",
             " |      ",
             " |      ",
             " |      ",
             "/ \     "],
        '7':["  ___   ",
             " |   |  ",
             "  |  O  ",
             " |   |  ",
             " |      ",
             " |      ",
             " |      ",
             "/ \     "],
        '8':["  ___   ",
             " |   |  ",
             "  |  O  ",
             "  | /|\ ",
             " |     ",
             " |      ",
             " |      ",
             "/ \     "],
        '9':["  ___   ",
             " |   |  ",
             "  |  O  ",
             "  | /|\ ",
             "  | / \ ",
             " |      ",
             " |      ",
             "/ \     "]
        }

window = tkinter.Tk()
window.geometry('400x500')
window.title('Gra Wisielec')

pom = tkinter.Label(window, text='')
pom.pack()

lbl = tkinter.Label(window, text='Wybierz poziom trudności:\n')

pom2 = tkinter.Label(window, text='')
pom2.pack()

glob_label = tkinter.Label(window, text=' \n\n\n\n\n\n\n\n')
glob_label.pack()
lbl.pack()

def disp_lbls():
    but = tkinter.Button(window, text='Start!',command=lambda: start())
    but.pack()

lvl=0
guesses=1
haslo = ''
slowo = ''
guessed_letters=''
game_on = True

def set_level(num):
    global lvl
    global haslo
    global slowo
    lvl = num
    choice1.destroy()
    choice2.destroy()
    choice3.destroy()
    slowo = lines[(lvl-1)*4+rand]
    haslo = '_ ' *((2*lvl)+2)
    lbl.configure(text = haslo, font=('Helvetica',16))
    entry.pack()
    but.pack()
    wprow_lab.pack()

def draw(num):
    i=0
    txt=''
    for i in range(8):
        txt=txt+str(drawing[str(num)][i])+'\n'
        i=i+1
    glob_label.configure(text=''+txt)

# main loop: reading entry letter, checking its occurence in solution,
# priting solution, drawing the drawing.

def start():
    global guesses
    global wprow
    global haslo
    global guessed_letters
    global game_on
    
    char = entry.get()
    entry.delete(0)
    guessed_letters = guessed_letters + char
    wprow = wprow + ' ' + str(char)
    wprow_lab.configure(text = wprow)

    haslo=''
    for letter in slowo:
        if char == letter or letter in guessed_letters:
            haslo = haslo + letter + ' '
        else:
            if letter != '\n':
                haslo = haslo + '_ '
                game_on = True
                
    lbl.configure(text = haslo)
    
    draw(guesses)

    if not game_on:
        info.configure(text='***** WYGRAŁEŚ *****\n* URATOWAŁEŚ WIEŚKA *')
        entry.destroy()
        but.destroy()
        window.quit()

    game_on = False
    guesses+=1
    if(guesses==11):
        info.configure(text='*** PRZEGRAŁEŚ ***\n* WIESIEK ZAWISŁ *')
        entry.destroy()
        but.destroy()

choice1 = tkinter.Button(window, text='Łatwy',command=lambda: set_level(1))
choice1.pack()
choice2 = tkinter.Button(window, text='Średni',command=lambda: set_level(2))
choice2.pack()
choice3 = tkinter.Button(window, text='Trudny',command=lambda: set_level(3))
choice3.pack()

f=open('Base.txt','r')
lines = f.readlines()
random.seed()
rand = random.randint(0,3)

info = tkinter.Label(window, text='\nZgadnij jaka litera znajduje sie w słowie-rozwiązaniu.\nKażda kolejna próba to krok do śmierci wisielca...')
info.pack()

entry = tkinter.Entry(window)
but = tkinter.Button(window, text='Check!',command=lambda: start())
wprow = 'Sprawdzono: '
wprow_lab = tkinter.Label(window, text=wprow)

window.mainloop()
