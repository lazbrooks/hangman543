import random

# Instate a list of words for the computer to pick from randomnly and the user to guess.
word_list = ["blimp", "blemish","perhaps", "glorify", "susurrus"]
# print(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []  # Empty list to store guessed letters
        self.word = random.choice(word_list).lower()  # Pick a word randomly from word_list
        self.word_guessed = ['_' for _ in self.word]  # Initialize word_guessed with underscores
        self.num_letters = len(set(self.word))  # Count of unique letters in the word

    def check_guess(self, guess):
        # format and test the latest input
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  # Replace '_' with the guessed letter
            self.num_letters -= 1  # Reduce the count of unique letters
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        # Gather a user input and test it is valid
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)


hangman_game = Hangman(word_list) 

print(hangman_game.word)
hangman_game.ask_for_input()