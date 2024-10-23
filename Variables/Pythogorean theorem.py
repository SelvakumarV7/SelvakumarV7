#Python uses the input() function to get user input:
#y default, the user input is stored as a text string.
#Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

#c=square root of a**2 + b**2
#Also, the square root of something is the same thing as power to the 0.5.

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = ((a**2) + (b**2))**0.5
print(c)

#Example 2: Quadratic formula

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))
root_1 = (-b + (((b**2) - 4*a*c)**0.5))/2*a
root_2 = (-b - (((b**2) - 4*a*c)**0.5))/2*a
print(root_1)
print(root_2)
