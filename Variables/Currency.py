#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Columbia = float(input('What do you have left in pesos?: '))
Peruvian = float(input('What do you have left in soles?: '))
Brazil = float(input('What do you have left in reais?: '))
B_C = float(Columbia*0.052)
B_P = float(Peruvian*0.27)
B_B = float(Brazil*0.18)
print("The Overall Balance in hand is: " , B_C + B_P + B_B)

