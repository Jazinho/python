import winsound

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

melodies = {"Dla_Elizy":"E200 D#200 E200 D#200 E200 h200 D200 C200 a400 sil100 c200 e200 a200 h400 sil100 e200 g#200 h200 C400 sil200 e200 E200 D#200 E200 D#200 E200 h200 D200 C200 a400 sil100 c200 e200 a200 h400 sil100 e200 C200 h200 a400"

            }

print(' ***** MUSIC MAKER ***** \n\n')

print('Type the note sign and its duration in miliseconds - simple as that!')
print('Example: c200 e100 g300 etc.')
print('Octave: \n')
print('______________________________________________________________')
print('| |   |   | | |   |   |   | | |   |   | | |   |   |   | |  |  ')
print('| | c#| d#| | | f#| g#| a#| | | C#| D#| | | F#| G#| A#| |  |  ')
print('| |___|___| | |___|___|___| | |___|___| | |___|___|___| |  |__')
print('|   |   |   |   |   |   |   |   |   |   |   |   |   |   |    |')
print('| c | d | e | f | g | a | h | C | D | E | F | G | A | H | CC |')
print('|___|___|___|___|___|___|___|___|___|___|___|___|___|___|____|')
print('\nComposed melodies: (type: \"<title>\")')
print('\n\"Dla_Elizy\"')

global note
global time
note = ''
time = ''
while(True):
    zapis = input('\nStart:')
    if zapis == '\"Dla_Elizy\"':
        zapis = melodies["Dla_Elizy"]
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
