import random
from hangman import hangman, art


# Load words from file
with open("words.txt", "r") as file:
    word_list = [line.strip() for line in file]

#Create word
word = random.choice(word_list).lower()


#On startup
print(art)
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
guessed_letters = set()

#print(word) #For debugging purposes
while not game_over:
    print("")
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    # Error Handling: Check if input is a single letter
    if not guess.isalpha():
        print("Invalid input! Please enter a letter (A-Z).")
        continue
    
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.add(guess)


    #guessing word
    if len(guess) == word_length:
        if guess == word:
        
            print(f"Congratulations! You guessed the word: {word}")
            break
        else:
            print("That's not the word.")

    elif len(guess) > 1:
        print("Your guess must be either one letter or the full word.")

            
    #guessing letter
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
        print(f"{' '.join(display)}")
    elif attempts == 0:
        game_over = True
        print("You lose!")
        print(f"The word was {word}")
    else:
        print("")
        print(f"You have {attempts} attempts left.")




