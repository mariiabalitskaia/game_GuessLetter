#!/usr/bin/env python

from random import choice


def game_agreement(list_of_word):
    guess_agreement = input(f"I hid a letter from one word from this list.\n"
                            f"Will you try to guess it? (yes/not) \n")
    if guess_agreement == "yes":
        print(f"Excellent! Lets try!")
        word = list(choice(list_of_word))
        letter = choice(word)
        word[word.index(letter)] = "?"
        letter_from_user = input(f"Word: {''.join(word)}\n"
                                 f"What letter is hidden?\n"
                                 f"Type letter: ")
        if letter_from_user == letter:
            print("You guess!")
        else:
            while letter_from_user != letter:
                if input(f"Try again: ") == letter:
                    print("You guess!")
                    break
    else:
        print("Ok.Bye.")


if __name__ == '__main__':
    game_agreement(['tower', 'human', 'computer', 'scissors'])
