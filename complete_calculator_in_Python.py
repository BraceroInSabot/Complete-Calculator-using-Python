# Imports
from math import sqrt
from colorama import (init, Fore, Back)

# User Inputs
print(Fore.YELLOW + "Python", Fore.BLUE + "Calculator!", Fore.RESET)
print()
print("SIGN:")
print()
print("Choose one of the respective signs below to make a math operation:")
print("1 - ' + ' \n2 - ' - ' \n3 - ' / ' \n4 - ' * ' \n5 - ' √ '")

try:
    sign = int(input('Then, write his number here: '))
    if sign > 5:
        print('Please, return and input only 1, 2, 3, 4 or 5')
        exit()
except (ValueError) as erra:
    print(f"There's something wrong with the 'User inputs' section: {erra}")

print()
print("PARAMETERS: ")
print()

try:
    param1 = int(input('Insert the 1º parameter here: \n'))
    if sign < 5:
        param2 = int(input('And then the 2º parameter here: \n'))
except (ValueError) as errb:
    print(f"There's something wrong with the 'User inputs' section: {errb}")

print()
print(Fore.BLUE + "Operation", Fore.YELLOW + "Result", Fore.RESET)
print()

# Execution
try:
    if sign == 1:


        def sum(x, y):
            """Returns the operation x + y"""
            return (x + y)
        
    
        print(f'You did {param1} + {param2} and it results in {sum(param1, param2)}')
    elif sign == 2:
        

        def subtraction(x, y):
            """Returns the operation x - y"""
            return (x - y)


        print(f'You did  {param1} - {param2} and it results in {subtraction(param1, param2)}')
    elif sign == 3:

    
        def division(x, y):
            """Returns the operation x / 1"""
            return (x / y)


        print(f'You did {param1} / {param2} and it results in {division(param1, param2)}')
    elif sign == 4:


        def multiplication(x, y):
            """Returns the operation x * y"""
            return (x * y)

    
        print(f'You did {param1} * {param2} and it results in {multiplication(param1, param2)}')
    else:


        def squareroot(x):
            """Returns the squareroot of the parameter"""
            return (sqrt(x))


        print(f'You did √{param1} and it results in {squareroot(param1)}') 
except (NameError, ValueError, ZeroDivisionError) as errc:
    print(f"There's something wrong with the 'Execution' sector: {errc}") 

"""Guilherme Bracero Gonzales, 29/11/2021"""
