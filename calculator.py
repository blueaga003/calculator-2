"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
import sys

def calculator_greeting():
    print("Welcome to the calcutor!")

def calculator_menu():
    print("You have the following options: add (a), minus (m), times (t), divide (d), square (s), cube (c), power (p), and remainder (r).")
    print("To see this menu again, type options (o)")
    print("To quit, type exit (e).")

def calculator_input():
    while True:
        print("You're in the calculator_input function.")
        user_input = input("> ")
        user_input = user_input.split(" ")
        user_option_choice = user_input[0][0].lower()

        try:
            number_1 = user_input[1]
            number_2 = user_input[2]
        except IndexError:
            if user_option_choice == "o":
                calculator_menu()
            elif user_option_choice == "e":
                print("Thanks for using the calculator!")
                sys.exit()
            elif user_option_choice not in "amtdscpr":
                print("This was not a valid option. Please try again.")
                calculator_menu()
                continue
            elif user_option_choice in "amtdpr":
                print("Please provide two numbers in addition to the function you are tying to perform.")
            elif user_option_choice == "c":
                print("Please provide one number in addition to the cube function.")
            user_input.extend([1,1])
            number_1 = int(user_input[1])
            number_2 = int(user_input[2])
        #    break        
        return user_option_choice, number_1, number_2

def calculator_operations(user_choice, input_number_1, input_number_2):
    while True:
        print("You're in the calculator_operations function.")
        print(input_number_1, input_number_2)
        if user_choice == "a":
            print(add(input_number_1, input_number_2))
        elif user_choice == "m":
            print(minus(input_number_1, input_number_2))
        elif user_choice =="t":
            print(times(input_number_1, input_number_2))
        elif user_choice =="d":
            print(divide(input_number_1, input_number_2))
        elif user_choice =="s":
            print(square(input_number_1))
        elif user_choice == "c":
            print(cube(input_number_1))
        elif user_choice == "p":
            print(power(input_number_1, input_number_2))
        elif user_choice == "r":
            print(remainder(input_number_1, input_number_2))
        elif user_choice == "o":
            calculator_menu()
        elif user_choice == "e":
            break
        else:
            print("This is not an option, please try again")

        user_choice, input_number_1, input_number_2 = calculator_input()


def run_calculator():
    calculator_greeting()
    calculator_menu()
    user_function_choice, user_from_input_1, user_from_input_2 = calculator_input()
    calculator_operations(user_function_choice, user_from_input_1, user_from_input_2)


run_calculator()
