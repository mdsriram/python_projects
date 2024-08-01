# Number Guessing Game

A simple Python-based number guessing game where the player tries to guess a randomly generated number within a specified range. The game provides feedback on whether the guessed number is too high or too low and tracks the number of guesses taken.

## Features

- Prompts the user to input the upper limit of the number range.
- Generates a random number within the specified range.
- Provides feedback on guesses (too high, too low, or correct).
- Counts and displays the number of guesses taken.

## Requirements

- Python 3.x

## Usage

1. **Run the Game**

   To start the game, simply run the Python script:

   ```bash
   python number_guessing_game.py

2. **Provide the Upper Limit**

When prompted, enter the upper limit of the range for the random number.
Type of number: 100

3. **Make Guesses**
   
The game will prompt you to make guesses until you guess the correct number. For each guess, you will receive feedback indicating whether your guess was too high, too low, or correct.
Make a guess: 50
You were below the number

5. **End of Game**
   
Once you guess the correct number, the game will print the number of guesses you took to find the correct number and end.
You got it in 7 guesses

## Notes

- Ensure you have Python 3.x installed on your machine.
- The game does not handle non-numeric input errors beyond basic checks.
- The upper limit must be a positive integer.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
