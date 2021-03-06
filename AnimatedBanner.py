import os
import time

dict = {'A':["  ***  ",
             " *   * ",
             " ***** ",
             " *   * ",
             " *   * "],
        'B':[" ****  ",
             " *   * ",
             " ****  ",
             " *   * ",
             " ****  "],
        'C':["  **** ",
             " *     ",
             " *     ",
             " *     ",
             "  **** "],
        'D':[" ****  ",
             " *   * ",
             " *   * ",
             " *   * ",
             " ****  "],
        'E':[" ***** ",
             " *     ",
             " ***** ",
             " *     ",
             " ***** "],
        'F':[" ***** ",
             " *     ",
             " ***** ",
             " *     ",
             " *     "],
        'G':["  ***  ",
             " *     ",
             " *  ** ",
             " *   * ",
             "  ***  "],
        'H':[" *   * ",
             " *   * ",
             " ***** ",
             " *   * ",
             " *   * "],
        'I':["   *   ",
             "   *   ",
             "   *   ",
             "   *   ",
             "   *   "],
        'J':["    *  ",
             "    *  ",
             "    *  ",
             " *  *  ",
             "  **   "],
        'K':[" *  *  ",
             " * *   ",
             " **    ",
             " * *   ",
             " *  *  "],
        'L':[" *     ",
             " *     ",
             " *     ",
             " *     ",
             " ***** "],
        'M':[" *   * ",
             " * * * ",
             " *   * ",
             " *   * ",
             " *   * "],
        'N':[" *   * ",
             " **  * ",
             " * * * ",
             " *  ** ",
             " *   * "],
        'O':[" ***** ",
             " *   * ",
             " *   * ",
             " *   * ",
             " ***** "],
        'P':[" ****  ",
             " *   * ",
             " ****  ",
             " *     ",
             " *     "],
        'R':[" ****  ",
             " *   * ",
             " ****  ",
             " *  *  ",
             " *   * "],
        'S':["  ***  ",
             " *     ",
             "  ***  ",
             "     * ",
             "  ***  "],
        'T':[" ***** ",
             "   *   ",
             "   *   ",
             "   *   ",
             "   *   "],
        'U':[" *   * ",
             " *   * ",
             " *   * ",
             " *   * ",
             " ***** "],
        'W':[" *   * ",
             " *   * ",
             " *   * ",
             " * * * ",
             " *   * "],
        'Y':[" *   * ",
             "  * *  ",
             "   *   ",
             "   *   ",
             "   *   "],
        'Z':[" ***** ",
             "    *  ",
             "   *   ",
             "  *    ",
             " ***** "],
        ' ':["     ",
             "     ",
             "     ",
             "     ",
             "     "]
        }

prt_msg=["",
         "",
         "",
         "",
         ""]

message = input('Give me text you want to float from right to left:\n')

#message to UPPER
message = message.upper()

for char in message:
    for i in range(5):
        prt_msg[i] += str(dict[char][i])


OFFSET = 76
WIDTH = 76

while(True):
    os.system('cls') #to clear screen
    for row in range(5):
        print(' '*OFFSET + prt_msg[row][max(0,OFFSET*-1):WIDTH - OFFSET])
    OFFSET -= 1
    time.sleep(0.03)
    if OFFSET == -(7*len(message)+1):
        OFFSET = WIDTH
    
