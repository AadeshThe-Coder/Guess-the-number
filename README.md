# Number Guessing Game

A simple command-line game written in Python. The computer picks a secret number between 1 and 100, and you try to guess it before you run out of tries.

## Features

- Two difficulty levels: **easy** (10 tries) and **hard** (5 tries)
- Hints after every guess: "Too high" or "Too low"
- Input checking, so typing a letter instead of a number won't crash the game
- Shows the secret number if you lose

## Requirements

- Python 3.6 or newer (no extra libraries needed)

## How to run

1. Download or clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/number-guessing-game.git
   cd number-guessing-game
   ```

2. Start the game:

   ```bash
   python3 number_guessing_game.py
   ```

   On Windows, use `python` instead of `python3`.

## How to play

1. Type `easy` or `hard` to choose a difficulty.
2. Enter a whole number between 1 and 100 for each guess.
3. Use the "Too high" and "Too low" hints to narrow it down.
4. Find the number before your tries run out to win.

## Example

```
Choose a difficulty (easy or hard): easy
I'm thinking of a number from 1 to 100. You have 10 tries.
Your guess: 50
Too high. 9 tries left.
Your guess: 25
Too low. 8 tries left.
Your guess: 37
You won!
```

## Ideas for improvement

- Ask the player if they want to play again
- Keep track of wins and losses across rounds
- Add a medium difficulty or let the player choose the number range
- Show a score based on how few tries were used

## What I learned

This was one of my first Python projects. It helped me practice loops, conditions, functions, user input and error handling.
