# This program simulates a game of Hangman
# It randomly selects a word from the parsed dictionary CSV file that is at least 5 letters long

import random
from random_vocab import load_words, choose_word


def play_hangman():
    words, definitions = load_words()
    word_to_guess = choose_word(words)
    word_index = words.index(word_to_guess)
    word_definition = definitions[word_index]
    guessed_letters = set()
    # Adjust attempts remaining based on difficulty
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    if difficulty == "easy":
        attempts_remaining = 10
    elif difficulty == "medium":
        attempts_remaining = 6
    elif difficulty == "hard":
        attempts_remaining = 4
    else:
        print("Invalid difficulty. Defaulting to medium.")
        attempts_remaining = 6

    while attempts_remaining > 0:
        display_word = "".join(
            [letter if letter in guessed_letters else "_" for letter in word_to_guess]
        )
        print(f"Word: {display_word}")
        print(f"Attempts remaining: {attempts_remaining}")
        guess = input("Guess a letter: ").strip().lower()

        # If the guess is not a single letter, prompt the user again
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # If user is on easy, reveal a random letter if it hasn't been guessed yet and if they have guessed twice incorrectly
        if (
            difficulty == "easy"
            and attempts_remaining <= 8
            and len(guessed_letters) >= 2
        ):
            unguessed_letters = [
                letter for letter in word_to_guess if letter not in guessed_letters
            ]
            if unguessed_letters:
                revealed_letter = random.choice(unguessed_letters)
                guessed_letters.add(revealed_letter)
                print(f"Hint: The letter '{revealed_letter}' has been revealed.")

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            print("Correct!")
            guessed_letters.add(guess)
        else:
            print("Incorrect.")
            guessed_letters.add(guess)
            attempts_remaining -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            print(f"Definition: {word_definition}")
            return

    print(f"Game over. The word was: {word_to_guess}")
    print(f"Definition: {word_definition}")


if __name__ == "__main__":
    play_hangman()
