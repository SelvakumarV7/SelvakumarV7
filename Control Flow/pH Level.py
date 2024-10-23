#Relational Operators:
#A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values

# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

pH = int(input("Enter the pH value(0-14): "))
if pH >=7:
    print('Basic')
elif pH < 7:
    print('Acidic')
else:
    print('Neutral')