#Loop:
#In programming, a loop is used to repeat a block of code until a specified condition is satisfied. It's another incredibly powerful tool that's used a ton!

#People will often use the generic term “iterate” when referring to loops; iterate simply means “to repeat”.

print('Welcome to Bank of India')

PIN = int(input('Enter Your ATM Pin: '))

while PIN != 1234:
    print('Incorrect Pin. Enter Correct PIN: ')
if PIN == 1234:
    print('Pin Accepted. Thank You')