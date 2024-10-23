#Create a coin_flip.py program

import random

num = random.randint(0,1)
if num > 0.5:
    print('Heads')
else:
    print('Tails')