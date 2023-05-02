import random

def word():
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(chosen_word)

    length_word = len(chosen_word)

    display = []
    for _ in range(length_word):
        display += "_"
    print(display)

    guess = input("guess a letter:- ").lower()

    for position in range(length_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)