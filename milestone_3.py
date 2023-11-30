import random

word_list = ["blimp", "blemish","perhaps", "glorify", "susurrus"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please choose a letter: ")

# if len(guess) == 1 and guess.isalpha():
#     print("Good guess!")
# else:
#     print("Oops! That is not a valid input.")


while True:
    guess = input("Please guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")