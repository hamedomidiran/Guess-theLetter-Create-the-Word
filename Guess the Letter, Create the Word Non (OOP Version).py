# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:22:09 2021

@author: tommywha
"""


import random
from IPython.display import clear_output


class GuessGame:
    colors = {
    'red':['roses','cherry','chili','blood','pomegranate'], 
    'blue':['flax','pansy','blueberries','macaw','flax'],
    'yellow':['macaroni','squash','butter','canary','dandelion'],
    }

    start_color = " "
    
    
    def __init__(self, item):   
        self.item = item
        
    def start_color(self):
        clear_output()
        print("\nPick a color below to guess a word in that color's category.\n")
        for k in self.colors.keys():
            print(f'-{k.title()}')
            
        start_color = input('What color would you like to start with:    ')
        
        if start_color.lower() in self.colors:
            print('\nThank you. The game starts now')
        else:
            while start_color.lower() not in self.colors:
                print('\nThat is not part of the option')
                start_color = input('\nWhat color do you want to start with:    ')   
            print('\nThank you. The game starts now')

        self.start_color = start_color
        
    def guess_color(self):
        clear_output()
        guess_word = random.choice(self.colors[self.start_color])
        
        counter   = 7
        right_ans = 0
        game = 'start'


        new_word = []
        used_words = []

        for i in range(len(guess_word)):
            new_word.append('_')
        
        print(' '.join(new_word))

        while game != 'over':
            users_guess = input('\nGuess a letter:    ')


            while len(users_guess) != 1:
                print('\nYour can only input one letter at a time')
                users_guess = input('\nGuess a letter:    ')

            users_guess = users_guess.lower()

            if users_guess in guess_word:
                if users_guess in used_words:
                    print('\nYou have inputted this letter before. Please try again')
                else:
                    for i in range(len(guess_word)):
                        used_words.append(users_guess)
                        if guess_word[i] == users_guess :
                            right_ans += 1
                            new_word[i] = users_guess

            else:
                if users_guess in used_words:
                    print('\nYou have inputed this letter before. Please try again')
                else:
                    used_words.append(users_guess)
                    counter     -= 1
                    print(f'\nYou have {counter}/7 guesses left')

            print(' '.join(new_word))

            if right_ans == len(guess_word):
                print('\nCongrats you won!\n')
                game = 'over'



            if counter == 0:
                game = 'over'
                print('\nThe game is over')


def Game():
    new_game = GuessGame([])
    while True:
        response = int(input('Type 1 to start a new game. \nType 2 to stop.\n'
                             '\n>>>>>>     '))
        while response != 1 and response != 2:
            print('\nSorry, that is not an option')
            response = input('Type 1 to start, Type 2 to stop.\n')
        if response == 1:
            new_game.start_color()
            new_game.guess_color()
        else:
            break
    
Game()
    
    