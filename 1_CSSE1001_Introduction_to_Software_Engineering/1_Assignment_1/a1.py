"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# My details
__author__ = "{{Xianglong LIN}} ({{45791439}})"
__email__ = "s4579143@student.uq.edu.au"
__date__ = "21/8/2020"

def select_word_at_random(word_select):
    """ Function which returns a string randomly selected from WORDS FIXED.txt or WORDS ARBITRARY.txt respectively

    Parameter:
        word_select(str): a string representing a FIXED or ARBITRARY word selection

    Return:
        word(str): a string representing the word being guessed by the player
    """
    
    # User input instruction is incorrect
    if word_select != 'FIXED' and word_select != 'ARBITRARY':
        return
    
    # Select word from 'FIXED' file or 'ARBITRARY' file
    else:
        words = load_words(word_select)
        index = random_index(words)
        word = words[index]
        return word        

def create_guess_line(guess_no, word_length):
    """ Function which returns the string representing the display corresponding to the guess number integer

    Parameters:
        guess_no(int): an integer representing how many guesses the player has made
        word_length(int): an integer representing the length of the word being guessed by the player

    Return:
        string(str): the string representing the display corresponding to the guess number integer
    """
    
    # Set variables
    index = GUESS_INDEX_TUPLE[word_length - 6]
    string = f'Guess {guess_no}' + WALL_VERTICAL

    # For loop which sets the guess line after the guess number 
    for i in range(word_length):

        # Use * to indicate the letter to be guessed in this round
        if index[guess_no - 1][0] <= i <= index[guess_no - 1][1]:
            string += ' * ' + WALL_VERTICAL
            
        # Use - to indicate the other letter and set spacing
        else:
            string += ' ' + WALL_HORIZONTAL + ' ' + WALL_VERTICAL

    # Return string
    return string

def display_guess_matrix(guess_no, word_length, scores):
    """ Function which prints the progress of the game

    Parameters:
        guess_no(int): an integer representing how many guesses the player has made
        word_length(int): an integer representing the length of the word being guessed by the player
        scores(tuple): a tuple containing all previous scores
        
    Return:
        None   
    """

    # Set the first line of the matrix
    # Word length is 6
    if word_length == 6:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 |')

    # Word length is 7
    elif word_length == 7:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')

    # Word length is 8   
    elif word_length == 8:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')

    # Word length is 9
    else:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
    print(WALL_HORIZONTAL * (9 + 4 * word_length))
    
    # Print the score line(s) and the segmentation line(s)
    for i in range(1, guess_no):
        print(create_guess_line(i, word_length) + '   ' + f'{scores[i - 1]} Points')
        print(WALL_HORIZONTAL * (9 + 4 * word_length))
        
    # Print the guess number line
    print(create_guess_line(guess_no, word_length))

    # Print the segmentation line
    print(WALL_HORIZONTAL * (9 + 4 * word_length))

def compute_value_for_guess(word, start_index, end_index, guess):
    """ Function which returns the score

    Parameter:
        word(str): a string representing the word the player has to guess 
        start_index(int): an integer the substring is created by slicing the word from
        end_index(int): an integer the substring is created by slicing the word up to and including 
        guess(str): a string representing the guess attempt the player has made

    Return:
        score(int): an integer, the player is awarded for a specific guess
    """
    
    # Set variables
    score = 0
    right_word = word[start_index : end_index + 1]

    # Calculate scores
    for i in range(len(guess)):

        # Each letter guessed in the correct position
        if guess[i] == right_word[i]:

            # Each vowel guessed in the correct position gets 14 points
            if guess[i] in VOWELS:
                score += 14

            # Each consonant guessed in the correct position gets 12 points
            else:
                score += 12

        # Each letter guessed correctly but in the wrong position gets 5 points        
        elif guess[i] in right_word:
            score += 5

    # Return score        
    return score

def main():
    """
    Handles top-level interaction with user.
    """

    # Greeting
    print (WELCOME)
    
    # Get user input
    start = input(INPUT_ACTION)
    
    # User input instruction does not match
    while start not in 'shq':
        print(INVALID)
        start = input(INPUT_ACTION)

    # Input h
    if start == 'h':
        print (HELP)

    # Input q
    elif start == 'q':
        return

    # Select word from file
    word_select = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")

    # User input instruction does not match   
    while word_select not in ('FIXED','ARBITRARY'):
        word_select = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")

    # Set variables
    word = select_word_at_random(word_select)
    word_length = len(word)
    scores = ()
    guess_no = 1

    # Start guessing word
    print('Now try and guess the word, step by step!!')

    # Test if user type is corrrect
    while guess_no <= word_length - 1:
        display_guess_matrix(guess_no, word_length, scores)
        start_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
        end_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]
        guess = input('Now enter Guess {}: '.format(guess_no))
        
        # User type letter length is incorrect
        while len(guess) != len(word[start_index : end_index + 1]):
            guess = input('Now enter Guess {}: '.format(guess_no))
        scores += (compute_value_for_guess(word, start_index, end_index, guess),)
        guess_no += 1

    # Set display guess matrix
    guess_no = word_length
    display_guess_matrix(guess_no, word_length, scores)

    # Get final guess
    final_guess = input('Now enter your final guess. i.e. guess the whole word: ')

    # Correct answer
    if final_guess == word:
        print('You have guessed the word correctly. Congratulations.')

    # Incorrect answer
    else:
        print('Your guess was wrong. The correct word was "{}"'.format(word))

if __name__ == "__main__":
    main()
