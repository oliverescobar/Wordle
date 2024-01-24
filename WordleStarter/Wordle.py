# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        current_row = gw.get_current_row()
        next_row = 0
        current_word = ""
        for col in range(N_COLS):
            current_word += gw.get_square_letter(current_row, col)
        if current_word in FIVE_LETTER_WORDS:
            gw.show_message('Good job. This is a word.')
            gw.set_current_row(next_row+1)
        else:
            gw.show_message("Not in the word list.")
            gw.set_current_row(next_row+1)




    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    randWord = random.choice(FIVE_LETTER_WORDS)
    print(randWord)

    for col in range(N_COLS):
        gw.set_square_letter(0, col, randWord[col])


# Startup code

if __name__ == "__main__":
    wordle()


# for letter in randRow: