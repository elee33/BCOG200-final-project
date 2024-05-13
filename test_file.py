
# Our wordle game will run in terminal. This code can be tested using pytest, mainly testing for if the code properly executes the basis of the game. 
# It should allow the user to enter their name, choose a language, and let the user guess 6 times. 
# Additionally, the check_place, get_guess, and evaluate_guess should properly execute and handle situations where some letters are not correct but in the right place, or when all of the letters are incorrect. 
# It also should be able to tell when the user is not using a five-letter word and allows them to retry until a valid guess is given. 

import random 
import time

def test_greet_user():
    print("Welcome to the Python version of Wordle!")
    time.sleep(2)
    username = input("What is your name? (Please type your name and press enter.) ")
    print("Hello, " + username.capitalize() + "! The rules are simple: ")
    time.sleep(2.5)
    print("Enter a FIVE-LETTER word from the given word bank. The word bank includes words related to science and/or bcog.")
    time.sleep(2.5)
    print("The code will let you know if letters are correct") 
    print("and/or correctly placed.")
    time.sleep(2.5)
    print(" ")
    time.sleep(2)

def test_ask_ready():
    return input("Are you ready? Y/N (cap-sensitive): ")

def test_choose_language():
    return input("English or Spanish? Click x to exit. (Please type English or Spanish to play the game in your desired language. Please type x and press enter to exit the game.) (case-sensitive) ")

def test_read_word_bank(language):
    filename = "wordle.txt" if language == "English" else "span_wordle.txt"
    with open(filename, "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        print(", ".join(words))
        return random.choice(words)

def test_check_place(char_g, char_w, place):
    if char_g == char_w:
        print(place + " letter: right letter, right place!")

def test_get_guess():
    guess = input("Enter a word: ")
    while len(guess) != 5:
        print("That was not a five-letter word!")
        guess = input("Enter a word: ")
    return guess

def test_evaluate_guess(guess, wordle):
    for i in range(5):
        if guess == wordle:
            print("You guessed it!")
            return True
        for j in range(5):
            if guess[i] == wordle[j]:
                if i == j:
                    print(f"{i + 1} letter: right letter, right place!")
                else:
                    print(f"{i + 1} letter: right letter, wrong place.")
                break
    return False

def test_play_game():
    test_greet_user()
    ready = test_ask_ready()
    if ready == "Y":
        language = test_choose_language()
        if language in ["English", "Spanish"]:
            wordle = test_read_word_bank(language)
            for _ in range(6):  # Allow 6 guesses
                guess = test_get_guess()
                if test_evaluate_guess(guess, wordle):
                    return
            print("You have used up your guesses. The Wordle was " + wordle + ".")
            print("Try again next time!")
        else:
            print("Bye!")
    elif ready == "N":
        print("Not ready yet? Please come back when you are! :) ")
    else:
        print("Invalid input.")

test_play_game()
