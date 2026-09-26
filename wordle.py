# This program simulates a game of Wordle

# It randomly selects a word from the parsed dictionary CSV file that is exactly 5 letters long
import random
import csv


def load_five_letter_words():
    five_letter_words = []
    with open("parsed_dictionary.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word = row[0].strip().lower()
            if len(word) == 5:
                five_letter_words.append(word)
    return five_letter_words


def select_random_word(five_letter_words):
    return random.choice(five_letter_words)


def tokenize_word(word):
    # Converts a word into a list of its individual letters with indices preserved
    return list(word)


def get_feedback(guess, secret_word):
    secret_tokens = tokenize_word(secret_word)
    guess_tokens = tokenize_word(guess)
    feedback = ["_"] * 5

    remaining = {}  # counts of secret letters not yet claimed by a green

    # First pass: greens, and tally up what's left over for yellows
    for i in range(5):
        if guess_tokens[i] == secret_tokens[i]:
            feedback[i] = guess_tokens[i].upper()
        else:
            remaining[secret_tokens[i]] = remaining.get(secret_tokens[i], 0) + 1

    # Second pass: yellows, left to right, only if a copy is still unclaimed
    for i in range(5):
        if feedback[i] == "_" and remaining.get(guess_tokens[i], 0) > 0:
            feedback[i] = guess_tokens[i]
            remaining[guess_tokens[i]] -= 1

    return feedback


def main():
    five_letter_words = load_five_letter_words()
    secret_word = select_random_word(five_letter_words)
    attempts = 6

    print("Welcome to Wordle!")
    print("You have 6 attempts to guess the 5-letter word.")
    print("If your letter is in the correct position, it will be shown in uppercase.")
    print(
        "If your letter is in the word but in the wrong position, it will be shown in lowercase."
    )
    print("If your letter is not in the word, it will be shown as an underscore ('_').")
    print("Let's begin!")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}: ").strip().lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        feedback = get_feedback(guess, secret_word)
        print("Feedback:", " ".join(feedback))
        if guess == secret_word:
            print("Congratulations! You've guessed the word correctly.")
            break
    else:
        print(f"Sorry! The correct word was '{secret_word}'.")


if __name__ == "__main__":
    main()
