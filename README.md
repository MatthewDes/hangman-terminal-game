# Hangman Game

A simple Hangman game built in Python that runs in the terminal. Players have six attempts to guess the correct word, either by guessing one letter at a time or the full word.

## Features
- Random word selection from a text file containing 100 words.
- ASCII art representation of the Hangman figure.
- Input validation to prevent duplicate or invalid guesses.
- Ability to guess letters or the full word.
- Clear game win/loss conditions with displayed results.

## Installation & Setup

1. **Clone the repository** or download the files manually:
   ```sh
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   ```

2. **Ensure you have Python installed** (Python 3 recommended). You can check by running:
   ```sh
   python --version
   ```

3. **Run the game**:
   ```sh
   python main.py
   ```

## File Structure
```
|-- hangman_game/
    |-- hangman.py   # Contains the Hangman ASCII art
    |-- words.txt    # List of words for the game
    |-- main.py      # Main game logic
    |-- README.md    # Project documentation
```

## How to Play
- The game randomly selects a word from `words.txt`.
- You have **6 attempts** to guess the word.
- You can guess **one letter** at a time or try to guess the **entire word**.
- If you guess a correct letter, it fills in the blanks.
- If you guess incorrectly, an attempt is lost, and the Hangman figure progresses.
- Win by guessing the word before your attempts run out.
- Lose if the Hangman figure is completed before you guess the word.

## Example Gameplay
```
Welcome to Hangman!
Try to guess the word in less than 6 attempts.
Good luck!

_ _ _ _ _
Guess a letter: a
_ a _ _ _
Guess a letter: e
_ a _ e _
Guess the word: table
Congratulations! You guessed the word: table
```

## Future Improvements
- Implement difficulty levels (easy, medium, hard).
- Create different different genres of words to choose from.
- Add a graphical user interface (GUI) version.
- Store player scores and allow replayability.

## Contributing
If you'd like to improve the game, feel free to fork the repository and submit a pull request! All feedback is welcome (good and bad)

## License
This project is open-source and free to use. Modify and distribute as you wish!


