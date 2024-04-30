import nltk
import os

# Append the current directory to the NLTK data path
nltk.data.path.append(os.getcwd())

# Import the words from the 'wordle.txt' file
with open("wordle.txt") as f:
    word_list = f.read().splitlines()

# Now you can use the 'word_list' variable containing the words from 'wordle.txt'

import random
import sys
from termcolor import colored

def print_menu():
    print("Let's play BCOG Wordle:")
    print("Type a 5 letter word and hit enter!\n")

def nltk_word():
    return random.choice(word_list)

print_menu()
play_again = ""
while play_again != "q":
    word = nltk_word()  # Choose word using NLTK corpus

    for attempt in range(1, 7): 
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(colored(f"Congrats! You got the wordle in {attempt} attempts", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {word}")

    play_again = input("want to play again? Type q to exit.") 
