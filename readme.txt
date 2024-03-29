1. For our project, we want to create a standard 5-letter wordle game with different categorical options that apply to our bcog200 course! The user will be able to select a category that the word will be from and receive 5 chances to guess the wordle correctly. After each guess, the user will receive an output of which letters they correctly guessed and if their position in the word is correct. 

2. 3 Functions:
  a. Choose Category Function - The user will be able to select from various psychology or neuroscience categories that their word will be from.
  b. Choose Word Function - Randomly generate a word from the provided vocabulary list within the category that the user has chosen.   This word will be used for the rest of the game.
  b. Is guess valid Function - This function will check if the input guess provided by the user is correct. There will be sub-functions within this function that will determine if the letters guessed are in the word and if the letters are in the correct place.

3. shriyadwivedi, varahatt, elee3, elliegp2

4. Group project
  a. The functions will be split up evenly, but we will collaborate to debug code. Each person will be responsible for 3-4 Functions of their choosing. 
  b. We will meet biweekly and discuss during class time to delegate work/responsibilities. Once a week, we will meet over the weekend to have time accounted for to work together on our project. 


Documentation/Outline of our game: 
We will be creating a wordle game that tests the user's knowlwedge of BCOG related terms that we have learned throughout this course and previous courses. 
Wordle is not only a popular game that many people play daily, but it is stimulatory for the brain and a good exercise. Our wordle game models the classic wordle from the New York Times, with the user having to type in a 5 letter word and receiving different colors (red, green, yellow) representing incorrect, correct, and misplaced letters. 
Our input data in the code will include a txt file of 5 letter BCOG related terms. 
In the code to guess a word, we will use a for function that includes an if guess to print colored letters green, and elif guess to print colored letters yellow and then 'else' to print the guess. 
If input word equals the correct word, then "Congrats! You got the wordle in {a certain amount of words}" will print in red. 
There will then be a print phrase "want to play again?" or "Type q to exit the game", for the user to follow.
Further on, we may use Tkinter or another python module to set up a visual of our wordle game in a 5x5 grid with the letters and corresponding colors depending on the guesses. 
