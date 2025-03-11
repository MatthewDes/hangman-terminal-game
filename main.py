import random
from hangman import hangman


# Load words from file
with open("words.txt", "r") as file:
    word_list = [line.strip() for line in file]

#Create word
word = random.choice(word_list).lower()


#On startup
print("Welcome to Hangman!")
print("Try to guess the word in less than 6 attempts.")
print("Good luck!")
print(hangman[0])

#Create a list of underscores
word_length = len(word)
display = []
for _ in range(word_length):
    display += "_"

#Game loop
game_over = False
attempts = 6
while not game_over:
    print("")
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    if len(guess) != 1:
        if guess == word:
            game_over = True
            print("You win!")
        elif len(guess) == len(word):
            print("That's not the word.")
            attempts -= 1
            print(hangman[6 - attempts])
        else:
             print("You can only guess one letter at a time.")
             continue

    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        attempts -= 1
        print(hangman[6 - attempts])

    if "_" not in display:
        game_over = True
        print("You win!")
        print(f"The word is {word}")
    elif attempts == 0:
        game_over = True
        print("You lose!")
        print(f"The word was {word}")
    else:
        print(f"You have {attempts} attempts left.")




