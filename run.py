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
            if guess in letters_guessed:
                print("You guessed already the letter", guess)
            elif guess not in word:
                print(guess, "its not in the word.")
                attempts -= 1
                letters_guessed.append(guess)
            else:
                print("Amazing Job", guess, "its in the word!")
                letters_guessed.append(guess)
                list_as_word = list(completion_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    list_as_word[index] = guess
                completion_word = "".join(list_as_word)
                if "_" not in completion_word:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print("You gussed already the word", guess)
            elif guess != word:
                print(guess, "its not the word.")
                attempts -= 1
                words_guessed.append(guess)
            else:
                guessed = True
                completion_word = word
        else: 
            print("Wrong guess")
        print(hangman_display(attempts))
        print(completion_word)
        print("\n")
    if guessed:
        print("Congratulation, you found the right word!! You Win!!!!")
    else:
        print("Ohh Sorry, you are out of attempte. The word was" + word + ". Hopfully next time you can get it!")


def hangman_display(attempts):
    """
    The stages we display for the hangman
    """
    stages = [  # final stage: head, torso, both arms and both legs
               """
                  --------
                  |      |
                  |      o
                  |     \\|/
                  |      | 
                  |     / \\
                  -
               """,
               # head, torso, both arms, and one leg
               """
                  --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
               """,
               # head, torso, and one arm
               """
                  --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # start with empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[attempts]


def main():
    """
    Main game to control and loop to try again
    """
    word = get_word()
    game(word)
    while input("Do you want to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        game(word)

    if __name__ == "__main__":
        main()