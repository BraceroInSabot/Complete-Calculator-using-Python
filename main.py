from math import sqrt
from time import sleep
from typing import Type
num1, num2, signal = Type[int], Type[int], Type[str]


def main() -> None:
    global num1, num2, signal
    try:
        num1 = int(input("1º number: "))
        signal = str(input("Signal (+, -, *, /, V): "))
        if signal == 'V':
            return resume()
        num2 = int(input("2º number: "))
    except (TypeError, ValueError, ZeroDivisionError) as err:
        print(f"Invalid Input! Try again. \n{err}")
        main()
    return resume()


def resume() -> None:
    if signal == "+":
        print(f"\n{num1} + {num2} = {num1 + num2}")
    elif signal == "-":
        print(f"\n{num1} - {num2} = {num1 - num2}")
    elif signal == "*":
        print(f"\n{num1} x {num2} = {num1 * num2}")
    elif signal == "/":
        print(f"\n{num1} / {num2} = {num1 / num2}")
    elif signal == "V":
        print(f"\n{sqrt(num1)} is the square root of {num1}")
    else:
        print("Invalid signal! Try again.")
        return main()
    sleep(2)
    print("Do you want to leave? y/n")
    out: str = str(input())
    if out == "y":
        exit()
    return main()


if __name__ == "__main__":
    main()
