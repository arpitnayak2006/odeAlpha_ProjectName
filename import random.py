import random

# List of predefined words
word_list = ["apple", "banana", "grape", "orange", "mango"]
chosen_word = random.choice(word_list)
guessed_word = ["_"] * len(chosen_word)  # Hidden word representation
attempts = 6  # Maximum incorrect guesses allowed
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("Word: " + " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    print("Word: " + " ".join(guessed_word))

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)