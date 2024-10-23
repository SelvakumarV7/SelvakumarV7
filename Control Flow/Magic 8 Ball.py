#Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

import random
Game = random.randint(1,9)
if Game == 1:
    print('Awesome')
elif Game == 2:
    print('Great')
elif Game == 3:
    print('Super')
elif Game == 4:
    print('wonderful')
elif Game == 5:
    print('Pakka')
elif Game == 6:
    print('Ok')
elif Game == 7:
    print('Marvellous')
elif Game == 8:
    print('Unbelievable')
else:
    print('All Good')