Python Wordle Game: BCOG Edition

1. For our BCOG200 course project, we have developed a Wordle game specifically themed around neuroscience and psychology. This Python-based game challenges players to guess a 5-letter word correctly within six attempts. The words are chosen from various categories relevant to our course content. After each guess, the player receives feedback through colors that indicate whether the letters are correct, misplaced, or incorrect. This version of Wordle is designed not only to be fun but also to enhance the player’s knowledge of BCOG-related terms.

2. 3 Functions:
  a. Choose Category Function - The user will be able to select from various psychology or neuroscience categories that their word will be from.
  b. Choose Word Function - Randomly generate a word from the provided vocabulary list within the category that the user has chosen.   This word will be used for the rest of the game.
  b. Is guess valid Function - This function will check if the input guess provided by the user is correct. There will be sub-functions within this function that will determine if the letters guessed are in the word and if the letters are in the correct place.

3. shriyadwivedi, varahatt, elee3, elliegp2

4. Group project
  a. The functions will be split up evenly, but we will collaborate to debug code. Each person will be responsible for 3-4 Functions of their choosing. 
  b. We will meet biweekly and discuss during class time to delegate work/responsibilities. Once a week, we will meet over the weekend to have time accounted for to work together on our project. 

5. Documentation/Outline of our game:
We have created a Wordle game that tests and expands the user's knowledge of BCOG-related terms from this and previous courses. Inspired by the classic New York Times Wordle, our game requires players to type in a 5-letter word from a provided word bank, which includes terms such as "brain," "nerve," and "ethic." The game supports both English and Spanish, allowing players to choose their preferred language at the start, which affects the word bank used during gameplay.

The game interface, developed in Python, provides feedback using colors—green for correct letters in the correct place, yellow for correct letters in the wrong place, and white for incorrect letters. If the player guesses the word correctly, the game congratulates them with a message in red, and asks if they wish to play again or exit. For incorrect attempts, the game informs the player of the correct word after their final guess and offers them a chance to try again or exit.

Our initial implementation runs in a terminal, but future enhancements might include implementing a graphical interface using Tkinter or another Python module. This interface would display a 5x5 grid, making the gameplay visually similar to the New York Times version, with letters and their corresponding colors based on the player’s guesses. The addition of the Spanish version not only broadens the accessibility of our game but also enhances the learning experience for students who are native Spanish speakers or are learning the language.

## Game Rules
1. Start the game by entering your name and selecting your preferred language.
2. Choose a 5-letter word from the prompted word bank.
3. You have 6 attempts to guess the right word. After each guess, the game will indicate which letters are correct or misplaced.
4. After 6 attempts, the game will reveal the correct word if not already guessed.
5. Players can choose to play again or exit the game after completing a wordle.

## Installation
To run this game, you'll need Python installed on your machine. Clone this repository and run `main.py` in your terminal or command prompt.
