# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from collections import Counter

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    def enter_action(s):
        current_row = gw.get_current_row()
        if current_row> N_COLS:
            gw.show_message(f'You have lost. The word was {sRandWord}')
        else:
            next_row = 0
            current_word = ""
            letter_count = 0
            for col in range(N_COLS):
                current_word += gw.get_square_letter(current_row, col)
            print(f"Word: {current_word}")
            current_word_counts = Counter(current_word.lower())
            sRandWord_counts = Counter(sRandWord)
            matched_letter_counts = Counter()

            word_length = len(current_word.strip())
            if word_length < 5:
                gw.show_message('Not enough letters. Please fill in more!')
                print(f'Word count is {word_length}')
            else:
                print(f'Word count is {word_length}')
                if current_word.lower() in FIVE_LETTER_WORDS:
                    gw.show_message('Good job. This is a word.')
                    for col, letter in enumerate(current_word.lower()):
                        print(f"col: {col}, letter: {letter}, sRandWord[col]: {sRandWord[col]}")
                        if letter == sRandWord[col]:
                            gw.set_square_color(current_row, col, CORRECT_COLOR)
                            gw.set_key_color(letter.upper(), CORRECT_COLOR)
                            matched_letter_counts[letter] += 1
                        elif letter in sRandWord and matched_letter_counts[letter] < sRandWord_counts[letter]:
                            gw.set_square_color(current_row, col, PRESENT_COLOR)
                            gw.set_key_color(letter.upper(), PRESENT_COLOR)
                            matched_letter_counts[letter] += 1
                        else: 
                            gw.set_square_color(current_row, col, MISSING_COLOR)
                            gw.set_key_color(letter.upper(), MISSING_COLOR)
                        
                    if current_word.lower() == sRandWord:
                        gw.show_message(f'Great job! The word was {sRandWord.upper()}')
                    else:
                        next_row = current_row+1  
                        if next_row == 6:
                            gw.show_message(f'You have lost. The word was {sRandWord}')
                        else:
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