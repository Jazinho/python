import winsound
import tkinter
from PIL import Image,ImageTk

sounds_freq = { 'c':523,
                'c#':554,
                'd':587,
                'd#':622,
                'e':659,
                'f':698,
                'f#':739,
                'g':783,
                'g#':830,
                'a':880,
                'a#':932,
                'h':987,
                'C':1046,
                'C#':1109,
                'D':1175,
                'D#':1245,
                'E':1319,
                'F':1397,
                'F#':1480,
                'G':1568,
                'G#':1661,
                'A':1760,
                'A#':1865,
                'H':1976,
                'CC':2093,
                'sil':37,
                }

def play():
    melodies = {"Dla_Elizy":"E200 D#200 E200 D#200 E200 h200 D200 C200 a400 sil100 c200 e200 a200 h400 sil100 e200 g#200 h200 C400 sil200 e200 E200 D#200 E200 D#200 E200 h200 D200 C200 a400 sil100 c200 e200 a200 h400 sil100 e200 C200 h200 a400",
                "Coco_Jumbo":"D200 F200 A400 sil100 D250 F100 A150 sil150 A300 D300 F200 A300 A#200 A200 G400 sil200 D200 F200 A400 sil100 D250 F100 A150 sil150 A300 G200 F100 G400 F200 sil200 F500 D200 F200 A400 sil100 D250 F100 A150 sil150 A300 D300 F200 A300 A#200 A200 G400 sil200 D200 F200 A400 sil100 D250 F100 A150 sil150 A300 G200 F100 G400 F200 sil200 F500",
                "Wlazł_Kotek":"G250 sil150 E200 sil150 E250 sil150 F300 sil150 D200 sil150 D250 sil150 C200 E200 G200 sil150 G400 C200 E200 G200 sil150 G400 G250 sil150 E200 sil150 E250 sil150 F300 sil150 D200 sil150 D250 sil150 C200 E200 C200 sil150 C400 C200 E200 C200 sil150 C400",
                "Oczy_Zielone":"a#400 sil200 g200 a#200 C200 C#400 C200 a#400 C400 g#400 sil800 F400 F#200 F400 sil400 a#400 sil150 g200 a#200 C200 C#400 C200 a#400 C400 g#400 sil800 F400 F#200 F400"
                }
    note = ''
    time = ''
    zapis = str(entry.get())
    if zapis == "Dla_Elizy":
        zapis = melodies["Dla_Elizy"]
    if zapis == "Coco_Jumbo":
        zapis = melodies["Coco_Jumbo"]
    if zapis == "Wlazł_Kotek":
        zapis = melodies["Wlazł_Kotek"]
    if zapis == "Oczy_Zielone":
        zapis = melodies["Oczy_Zielone"]
    for char in zapis:
        if char.isdigit():
            time = time + char
        elif char == ' ':
            winsound.Beep(sounds_freq[note],int(time))
            note=''
        else:
            note = note + char
            time = ''
    winsound.Beep(sounds_freq[note],int(time))
    note = ''
    time = ''
    zapis= ''

window = tkinter.Tk()
window.title('Meldodie maker & Music Challenger')
window.geometry('700x500')
window.wm_iconbitmap('favicon.ico')

img = ImageTk.PhotoImage(Image.open("piano_key.png"))
panel = tkinter.Label(window, image = img)
panel.pack()

info = tkinter.Label(window, text = '\nWprowadź oznaczenie nuty oraz długość dźwieku w milisekundach, aby zagrać dany dźwięk.\nAby zagrać melodię wprowadź całą sekwencję, np. e200 g300 h#100.\nCiszę oznaczono jako \'sil\'\n')
info.pack()
entry = tkinter.Entry(window, width=80)
entry.pack()
but = tkinter.Button(window, text="Zagraj!", command=lambda: play(),height=2,width=10)
but.pack()
melodies = tkinter.Label(window, text="\nBy odegrać gotowe melodie, wpisz poniższe tytuły.\n\nDla_Elizy\nCoco_Jumbo\nWlazł_Kotek\nOczy_Zielone")
melodies.pack()

window.mainloop()

