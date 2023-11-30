import random

# Instate a list of words for the computer to pick from randomnly and the user to guess.
word_list = ["blimp", "blemish","perhaps", "glorify", "susurrus"]
# print(word_list)

word = random.choice(word_list)
print(word)


def ask_for_input():
# Gather a user unput and test it is valid
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


def check_guess(current_guess):
# format and test the latest input
    current_guess = current_guess.lower()
    if current_guess in word:
        print(f"Good guess! {current_guess} is in the word.")
    else:
        print(f"Sorry, {current_guess} is not in the word. Try again.")

ask_for_input()