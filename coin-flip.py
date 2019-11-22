'''
Simulates a coin flip and returns the results
'''

import random

def flip():
    
    heads = 0
    tails = 0
    
    while True:

        choice = input('Press ENTER to flip the coin or enter any character to end the program\n')
        
        if choice == '':
            
            result = random.randint(0,1)

            if result == 0:
                heads += 1
                print(f'HEADS\nTotal Heads: {heads}\nTotal Tails: {tails}')
                continue

            else:
                tails += 1
                print(f'TAILS\nTotal Heads: {heads}\nTotal Tails: {tails}')
                continue
        else:
            
            break
            
flip()
