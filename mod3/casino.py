import random
import time

kierros = 0

prompt1 = input('Flip a coin? y/n:\t')


while prompt1 == 'y':

    print('Flipping coin...')
    time.sleep(1)

    kierros += 1
    print(f'Kierros {kierros}')

    luku = random.randint(1,2)
    if luku == 1:
        print('Heads!')
    else:
        print('Tails!')
    
    prompt2 = input('Try again? y/n\t')
    if prompt2 == 'n':
        print('See you soon!')
        break
        
