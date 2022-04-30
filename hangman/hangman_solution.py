'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from operator import index
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''


    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['-'] * len(self.word)
        self.list_letters = []
        self.num_letters = len(self.word)
        self.hangman_viz = ['''
   +---+
   O   |
  /|\  |
  / \  |
       ===''','''
   +---+
   O   |
  /|\  |
  /    |
      ===''','''
   +---+
   O   |
  /|\  |
       |
      ===''','''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''','''
   +---+
       |
       |
       |
      ===''']
        print(f"The mistery word has {self.num_letters} characters")
        print(f"You have {self.num_lives} lives")
        print(f"{self.word_guessed}")
        

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        letter = str.lower(letter)
        if letter in self.word:
            self.num_letters -= 1
            self.list_letters.append(letter)

            index = self.word.index(letter)
            del self.word_guessed[index]
            self.word_guessed.insert(index, letter)
            try:
                count = index
                for i in range(len(self.word)):
                    index = self.word.index(letter, count)
                    del self.word_guessed[index]
                    self.word_guessed.insert(index, letter)
                    count += 1
            except:
                pass
            print(f"Nice! {letter} is in the word!")
            print(f'{self.word_guessed}')
        else:
            self.num_lives -= 1
            self.list_letters.append(letter)
            print(f"Sorry, {letter} is not in the word")
            print(f'{self.hangman_viz[self.num_lives]}')
            if self.num_lives == 1:
                print(f"You have {self.num_lives} chances left")
            elif self.num_lives == 0:
                pass
            else:
                print(f"You have {self.num_lives} chances left")

        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter = input('Enter a single character >> ')
            if len(letter) != 1 and letter.isalpha():
                print('Please, enter just one character')
            elif letter == 1 and letter in self.list_letters:
                print(f'{letter} was already tried')
            elif len(letter) == 1 and letter not in self.list_letters:
                print("\nThat's right!")
                break
            else:
                print('Please, enter a character')
        self.check_letter(letter)

def play_game(word_list):
    # As an aid, part of the code is already provided:
    print("WELCOME TO THE HANGMAN GAME. LET'S GO!")
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}.")
            break
        elif game.num_letters > 0:
            game.ask_letter()
        else:
            print('Congratulations! You won!')
            break  

    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"



if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
