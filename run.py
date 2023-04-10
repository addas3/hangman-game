import random
from listwords import list_word

def get_word():
    """
    Getting the word from the listword and chaning it to uppercase
    """
    word = random.choice(list_word)
    return word.upper()




