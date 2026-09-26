# This program checks the definitions of a word the user inputs against parsed_dictionary.csv

import random_vocab


def check_definition(word):
    words, definitions = random_vocab.load_words()
    if word in words:
        word_index = words.index(word)
        return definitions[word_index]
    else:
        return None


def main():
    while True:
        word = (
            input("Enter a word to check its definition (or 'quit' to exit): ")
            .strip()
            .lower()
        )
        if word == "quit":
            break
        definition = check_definition(word)
        if definition:
            print(f"Definition of '{word}': {definition}")
        else:
            print(f"Word '{word}' not found in the dictionary.")


if __name__ == "__main__":
    main()
