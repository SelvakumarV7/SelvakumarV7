#Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are and, or, and not operators:

#Create a new file called the_cyclone.py.

#Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

Height = int(input('Enter your Height: '))
Credit = int(input('Enter your Credit: '))
if Height == 137 and Credit == 10:
    print("Enjoy the Ride")
elif Height < 137 and Credit == 10:
    print('Your are not Tall enough to ride')
elif Height == 137 and Credit < 10:
    print("You don't have not enough Credits")
else:
    print('You not meet the requirement!')