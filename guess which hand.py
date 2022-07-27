import random
Line_Length =15
word = 's'

cups = int(input('How many cups do you need for game?:  ')) #cups for hidding
user_guess = int(input('How many guess do you want to have?:  ')) #On the other hand,user_guess is number of round of match
AI_gusses = random.randint(1,cups)
print('-'*Line_Length)

for i in range(user_guess):
    if user_guess - i==1:
        word=''
    print(f'{user_guess - i} chance{word} left')
    user_input=int(input(f'Guess [1-{cups}]: '))
    if user_input==AI_gusses:
        print('you guess right!')
        break 
    else:
        print('you guess wrong .')
        print('-'*Line_Length)        

if user_input==AI_gusses:
    print('you won!')
    
else:
    print('you lost Sorry.')
    print(f'right answer was {AI_gusses}')



