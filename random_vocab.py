import csv
import random


def load_words(file_path="parsed_dictionary.csv"):
    words = []
    definitions = []
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row: Word, Definition
        for row in reader:
            if len(row) >= 2:
                word = row[0].strip()
                word = row[0].strip().lower()
                definition = row[1].strip()
                if len(word) >= 5:
                    words.append(word)
                    definitions.append(definition)
    return words, definitions


def choose_word(words):
    return random.choice(words)
