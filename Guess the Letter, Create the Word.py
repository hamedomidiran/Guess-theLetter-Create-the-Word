import random

colors = {
    'red':['roses','cherry','chili','blood','pomegranate'], 
    'blue':['flax','pansy','blueberries','macaw','flax'],
    'yellow':['macaroni','squash','butter','canary','dandelion'],
}

done = True

while done == True:
    print("\nPick a color below to guess a word in that color's category.\n")
    for k in colors.keys():
        print(f'-{k.title()}')

    start_color = input('What color would you like to start with:    ')

    if start_color.lower() in colors:
        print('\nThank you. The game starts now')
    else:
        while start_color.lower() not in colors:
            print('\nThat is not part of the option')
            start_color = input('\nWhat color do you want to start with:    ')   
        print('\nThank you. The game starts now')

    start_color = start_color.lower()

    guess_word = random.choice(colors[start_color])

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


        if game == 'over':
            print('\nWould you like to play again?')
            end = input('Yes/No:     ')
            
            while end.lower() != 'yes' and end.lower() != 'no':
                print('\nThat is not an option')
                print('\nWould you like to play again?')
                end = input('\nYes/No:     ')
            
            if end.lower() == 'yes':
                done = True
            else:
                done = False
