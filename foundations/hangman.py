
# part 1
import random
import sys
from colorama import Fore, Style
max_errors = 8


class HangmanLexicon():
    def __init__(self):
        self.lexicon = {
            0: "BUOY",
            1: "COMPUTER",
            2: "CONOISSEUR",
            3: "DEHYDRATE",
            4: "FUZZY",
            5: "HUBBUB",
            6: "KEYHOLE",
            7: "QUAGMIRE",
            8: "SLITHER",
            9: "ZIRCON"
        }

    def get_word_count(self):
        return len(self.lexicon.keys())

    def get_word(self, i):
        return self.lexicon[i]


class Hangman():
    def __init__(self, max_errors=max_errors):
        self.lexicon = HangmanLexicon()
        self.max_errors = max_errors
        self.errors = None

    def run(self):
        self.secret_index = random.randint(0, 9)
        self.secret_word = self.lexicon.get_word(self.secret_index)
        self.errors = 0
        self.state = '_' * len(self.secret_word)
        self.correct_list = []
        print("Welcome to angman!")
        while self.errors < self.max_errors:
            if self.state != self.secret_word:
                print(f"The word now looks like this : {Fore.GREEN}{self.state}{Style.RESET_ALL}")
                if self.max_errors - self.errors > 1:
                    print(f"You have {self.max_errors - self.errors} guesses left.")
                else:
                    print("You have only one guess left.")
            else:
                print(f"You guessed the word: {Fore.GREEN}{self.secret_word.upper()}{Style.RESET_ALL}.")
                print("You win.")
                break
            letter = input(f"Your guess: {Fore.GREEN}")
            print(f"{Style.RESET_ALL}", end="")
            if letter.upper() in self.secret_word:
                print("That guess is correct.")
                self.correct_list.append(letter.upper())
                self.state = "".join([l if l in self.correct_list else "_" for l in self.secret_word])
            else:
                print(f"There are no {letter.upper()}'s in the word.")
                self.errors += 1
        else:
            print("You're completely hung.")
            print(f"The word was: {Fore.GREEN}{self.secret_word.upper()}{Style.RESET_ALL}")
            print("You lose.")


if __name__ == "__main__":
    game = Hangman()
    game.run()


