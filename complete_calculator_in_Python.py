# Imports
from math import sqrt
from colorama import Fore

# Code
print(Fore.YELLOW + "Python", Fore.BLUE + "Calculator!", Fore.RESET)
print()
print("SIGN:")
print()
print("Choose one of the respective signs below to make a math operation:")
print("1 = ' + ' \n2 = ' - ' \n3 = ' / ' \n4 = ' * ' \n5 = ' √ '")

# User Signal Input
sign: int = 0


def signals():
    global sign
    try:
        sign = int(input('Then, write his number here: '))
        if sign > 5:
            print('Please, return and input only 1, 2, 3, 4 or 5')
            return signals()
        return userinputs()
    except ValueError as erra:
        print(f"You may use only int numbers. {erra}")
        return signals()


param1: int = 0
param2: int = 0


# User Number input
def userinputs() -> int:
    global param1, param2
    try:
        param1 = int(input('\nInsert the 1º parameter here: \n'))
        if sign < 5:
            param2 = int(input('And the 2º here: \n'))
            return True
        return True
    except ValueError as errb:
        print(f"You may use only float numbers. {errb}")
        return userinputs()


# Execution
def operation(p1: int, p2: int):
    global sign
    print("\nRESULT:\n")
    try:
        if sign == 1:
            return print(f"{p1 + p2}")
        elif sign == 2:
            return print(f"{p1 - p2}")
        elif sign == 3:
            return print(f"{p1 // p2}")
        elif sign == 4:
            return print(f"{p1 * p2}")
        else:
            ret = sqrt(p1)
            round(ret)
            return print(f"~{ret}")

    except (NameError, ValueError, ZeroDivisionError) as errc:
        print(f"There's something wrong with the operation: {errc}")
        return userinputs()


# Exec
if __name__ == '__main__':
    signals()
    operation(p1=param1, p2=param2)
