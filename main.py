import random
import sys
from termcolor import colored
import nltk

nltk.download('words')
from nltk.corpus import words

def print_menu():
    print("Let's play BCOG Wordle:")
    print("Type a 5 letter word and hit enter!\n")

def nltk_word():
    pass # You can add code here if needed

def read_word():
    with open("wordle.txt") as f:
        words = f.read().splitlines()
    return random.choice(words)

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print_menu()
play_again = ""
while play_again != "q":
    #word = read_word()
    word = random.choice(words_five)

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
            print(colored(f"Congrats! You got the wordle in {i}", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {word}")
    play_again = input("want to play again? Type q to exit.")
