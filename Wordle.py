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
        if current_row>= N_COLS:
            gw.show_message(f'You have lost. The word was {sRandWord}')
        else:
            next_row = 0
            current_word = ""
            for col in range(N_COLS):
                current_word += gw.get_square_letter(current_row, col)
            print(f"Word: {current_word}")

            word_length = len(current_word.strip())
            if word_length < 5:
                gw.show_message('Not enough letters. Please fill in more!')
                print(f'Word count is {word_length}')
            else:
                print(f'Word count is {word_length}')
                if current_word.lower() in FIVE_LETTER_WORDS:
                    gw.show_message('Good job. This is a word.')
                    next_row = current_row+1
                    gw.set_current_row(next_row)
                else:
                    gw.show_message("Not in the word list.")

    gw = WordleGWindow()
    sRandWord=random.choice(FIVE_LETTER_WORDS)
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":

    wordle()

# Hello Josh

# THis is my second change