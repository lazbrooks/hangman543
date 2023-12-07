import random

# Instate a list of words for the computer to pick from randomnly and the user to guess.
list_of_words = ["blimp", "blemish","perhaps", "glorify", "susurrus"]


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []  # Empty list to store guessed letters
        self.word = random.choice(word_list).lower()  # Pick a word randomly from word_list
        self.word_guessed = ['_' for _ in self.word]  # Initialize word_guessed with underscores
        self.num_letters = len(self.word)  # Count of unique letters in the word

    def check_guess(self, guess):
        # format and test the latest input
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  # Replace '_' with the guessed letter
                    self.num_letters -= 1
                    print(self.word_guessed)
                    print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        # Gather a user input and test it is valid
        while True:
            guess = input("Please guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break




def play_game(word_list):
    num_lives = 4
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(list_of_words)