import random

def random_word():
    words = open('words.txt', mode ="r",encoding='utf-8')
    words = words.read()
    words_list= words.split('\n')
    words = random.randint(0, len(words_list)) 
    choosed_word = words_list[words]
    return choosed_word
    
def hang_graph():
    print(HANGED[0])
    print((len(random_word())) * '_ ')
    
def correct_word():
   attempts = 0

   while attempts < 6:
    letter = input('Print a letter: ')
    attempts = attempts + 1
    print(attempts)

    if attempts == 6:
     print('You lose, better luck in the next time!')
     break

  
   

    
    
  

menu="""
_________________________________________
          WELCOME TO HANG GAME

  You have six attempts to win this game 

The program choose a word in ramdom order
and your job is guess what word is or the
little person on the hang DIE!!!

               LETS PLAY
_________________________________________

Select the difficult:

 1) Easy
 2) Medium
 3) Hard

R//:  """

difficult = int(input(menu))



HANGED = ['''
   +---+
   |   |
       |
       |
       |
       |
=============''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========''']


