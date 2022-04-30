# Hangman-Word_Game_Project

This is a simple hangman game. It was written in python language, using the class method. To play, just guess a letter by typing your guess on your keyboard. If you guess incorrectly 5 times, you lose. If you guess the word before that happens, you win.
Below is a flow of how the game is programmed:
First, the class Hangman is defined - <class Hangman>
Next, the game attributes, including number of lives, list of words to be selected randomly, a list of of letters of the word guessed represented initially by dash. The __init__ method is used to initialise all attributes that are relevant to implementing the game.

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
        print(f"{self.word_guessed}") '''
  
  next, the rule of the game is defined using the check_letter method.
  
  '''
  def check_letter(self, letter) -> None:'''
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
                print(f"You have {self.num_lives} chances left")'''

  
Next, the instructional guidance to the player is defined using the ask_letter method. This guides the player on how to play the game. The player's input is validated by calling the check_letter method.
  '''
  def ask_letter(self):'''
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
        self.check_letter(letter)'''
  
Now, the code required to start playing the game is inserted and by calling the class Hangman:
 ''' 
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
  
  if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)'''
