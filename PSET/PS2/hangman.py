 # Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for x in secret_word:
        print("a")
        
        print(x in letters_guessed)
        print("b")
        if x in letters_guessed == True:
            print(f'x= {x}, letters = {letters_guessed}, {secret_word}')
            print(x in letters_guessed)
        else:
            print("f")
            return False
    
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    q=""

  
    for x in secret_word:
        if x in letters_guessed:
            q = q+x+" "
        else:
  
            q = q+"_"+" "
            

            
    y=q[0:(len(q)-1)]
    
    return y
            
        
        
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
 
    
    x = string.ascii_lowercase
    
    for q in letters_guessed:
       x = x.replace(q,"")
    
    return x
    
def input_check(user_input, wornings, guesses, letters_guessed):   
    
    """ 
    the function checks if user input is valid. valid input is a lowercase or uppercase letter,
    it is only one character and should not be guessed before.
    
    input: user input (str), number of wornings left (int)
    
    returns: letter guessed (str), number of wornings left (int), number of guesses left (int)
    
    """
    if (len(user_input) == 1) and (user_input.lower()) and (user_input.isalpha()) and (user_input not in letters_guessed):
            pass
    else:
        wornings=wornings-1
        if wornings!=0:
            print(f"This is the worning. Your input should have only one alphabet letter, which was not yet guessed - try again. You have {wornings} wornings left before you loose the guess.")
            
        else:
            guesses = guesses-1
            wornings=3
            print("This is the worning. Your input should have only one alphabet letter, which was not yet guessed - try again. You have no wornings - You are loosing a guess this time.")
        return (False , user_input, wornings, guesses, letters_guessed)
    
    letters_guessed.append(user_input)
    
    return (True, user_input, wornings, guesses, letters_guessed)

def score(secret_word):
    
    letters = []
    counter=0
    
    for letter in secret_word:
        if letter not in letters:
            letters.append[letter]
            counter += 1
        else:
            pass
    return counter
        
        
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

    print(f"Welecome to hangman game! The word you're guessing has {len(secret_word)} letters. Wish you luck!")
    
    g = 6
    letters_guessed=[]
    wornings = 3
    
    while g>0 :
        
        print(f"You have {wornings} remaining wornings")
        print(f"You have {g} remaining guesses")
        word= get_guessed_word(secret_word, letters_guessed)
    
        print(f"Your word is: {word}")
        
        li= get_available_letters(letters_guessed)
        print(f"The letters you haven't guess yet are: {li}")
        

        
        q = input("Please guess the letter (remember to choose one letter at the time!):")
        
        c, q, wornings, g, letters_guessed = input_check(q, wornings, g, letters_guessed)
        print(f'c, q, wornings, g, letters_guessed = {c, q, wornings, g, letters_guessed}')
        
        if c==True:
            
        
            if q in secret_word:
                               
                print(f"Good choice, your letter \"{q}\" is in the secret word.")
                if is_word_guessed(secret_word, letters_guessed)==True:
                    print("Congrats, you found the whole word!")
                    word= get_guessed_word(secret_word, letters_guessed)
                
                    print(f"Your word is: {word}")
                    
                    final = g * (score(secret_word))
                    print(f'You gained {final} points, congratulations!')
                    
                    break
            else:
                print(f"Poor choice, your letter \"{q}\" is not in the secret word.")
                if q in "aoieuy":
                    g=g-2
                else:
                    g=g-1
                
            
        if g == 0:
             print("So sorry you lost, you have no guesses left")
             print(f"You've been looking for the word: {secret_word}")
             break
                
        

            
        print("-----------------------------------------")
        
            
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
