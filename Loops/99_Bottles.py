#This can be done in Python using string concatenation.

for i in range(5):
    print('The Square of ' + str(i) + ' is ' + str(i*i))

#String Interpolation:
#String interpolation is a process of substituting values of variables into placeholders in a string.
#For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, nice to meet you!', you would like to replace the placeholder {name} with an actual name. This is string interpolation.
#The above program can be recreated using string interpolation using the {} sign


for i in range(5):
    print(f'The Square of {i} is {i*i}')

#99 beers on wall:

for i in range(99, 0, -1):
    print(f'{i} Bottles of Beer on the wall')
    print(f'{i} Bottles of beer')
    print('Take one down, pass it around')