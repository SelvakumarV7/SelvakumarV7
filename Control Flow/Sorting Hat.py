#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to
#Write a program that asks the user some questions with the int() and input() functions

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print('''_________The Sorting Hat_________
                                
                                        
                                            ''')
print('Q1) Do you like Maggi or Yipee?: ')
print('1) Maggi')
print('2) Yipee')
Answer = int(input('Your Answer is(1-2): '))
if Answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif Answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input')

print('Q2) I want people to remind me as: ')
print('1) The Good')
print('2) The Great')
print('3) The Amazing')
print('4) The Awesome')
Answer_2 = int(input('Your answer is(1-4): '))
if Answer_2 == 1:
    Hufflepuff +=2
elif Answer_2 == 2:
    Slytherin += 2
elif Answer_2 == 3:
    Ravenclaw += 2
elif Answer_2 == 4:
    Gryffindor += 2
else:
    print('Wrong Input')

print('Q3) Which brand you like in Mobile?: ')
print('1) Apple')
print('2) Samsung')
print('3) Oneplus')
print('4) Redmi')
Answer_3 = int(input('Your answer is(1-4): '))
if Answer_3 == 1:
    Slytherin += 4
elif Answer_3 == 2:
    Hufflepuff += 4
elif Answer_3 == 3:
    Ravenclaw += 4
elif Answer_3 == 4:
    Gryffindor += 4
else:
    print('Wrong input')

print('Gryffindor points: ' , Gryffindor)
print('Ravenclaw points: ' , Ravenclaw)
print('Hufflepuff points: ' , Hufflepuff)
print('Slytherin points: ' , Slytherin)

max_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if Gryffindor == max_points:
    print('Gryffindor is Maximum: ' , Gryffindor)
elif Ravenclaw == max_points:
    print('Ravenclaw is Maximum: ' , Ravenclaw)
elif Hufflepuff == max_points:
    print('Hufflepuff is Maximum: ', Hufflepuff)
else:
    print('Slytherin is Maximum: ', Slytherin)