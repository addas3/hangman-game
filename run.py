import random
from listwords import list_word

def get_word():
    """
    Getting the word from the listword and chaning it to uppercase
    """
    word = random.choice(list_word)
    return word.upper()

def game(word):
    """
    The base of the game where it have the welcome message and the while loop
    """
    completion_word = "_" * len(word)
    guessed = False
    words_guessed = []
    letters_guessed = []
    attempts = 6
    print("Welcome to Hangman!")
    print("Rules are simple guess the word before the hangman is fully drawn!")
    print(hangman_display(attempts))
    print(completion_word)
    print("Let's start the game!")
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a word or a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():

        elif len(guess) == len(word) and guess.isalpha():

        else: 
            print("Wrong guess")
            print(hangman_display(attempts))
            print(completion_word)
            print("\n")




