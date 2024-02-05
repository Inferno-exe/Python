def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        print("Can't divide by Zero.")
        exit()
    return num1 / num2 

from math import *
def calculate_powers(num1, num2):
    return num1 ** num2

def calculator():
    print("Hey, I'm your calculator. What would you like to do today?\n I can do Add, Subtract, Multiply, Divide, and Calculate Powers & Square root.\n")
    option = input("Add/Subtract/Multiply/Divide/Powers/Root: ")

    try:
        if option in ["Add", "Subtract", "Multiply", "Divide"]:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
        elif option in ["Powers"]:
            num1 = int(input("Base number: "))
            num2 = int(input("Power: "))
        elif option in ["Root"]:
            num1 = int(input("Base number: "))
        else:
            print("Incorrect input, try again. ")
            return
    except ValueError:
        print("Invalid input, try again. ")
        exit()

    if option == "Add":
        result = add_numbers(num1, num2)
        print("\nCalculating " + str(num1) + " + " + str(num2) + ":")
    elif option == "Subtract":
        result = subtract_numbers(num1, num2)
        print("\nCalculating " + str(num1) + " - " + str(num2) + ":")
    elif option == "Multiply":
        result = multiply_numbers(num1, num2)
        print("\nCalculating " + str(num1) + " * " + str(num2) + ":")
    elif option == "Divide":
        result = divide_numbers(num1, num2)
        print("\nCalculating " + str(num1) + " / " + str(num2) + ":")
    elif option == "Powers":
        result = calculate_powers(num1, num2)
        print("\nCalculating " + str(num1) + "^" + str(num2) + ":")
    elif option == "Root":
        result = sqrt(num1)
        print("              ___")
        print("Calculating _/" + str(num1) + ":")
    else:
        print("Wrong input, try again. ")

    print("Answer = " + str(result) + "\n")

calculator()
