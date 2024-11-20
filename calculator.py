import math
from colorama import Fore, init, Style
import time

init(autoreset=True)

def print_gradient_text(text):
    colors = [Fore.MAGENTA]
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='', flush=True)
        time.sleep(0.002) 
    print()

def get_float_input(prompt):
    """Функция для безопасного ввода числового значения."""  
    while True:
        try:
            value = input(Fore.MAGENTA + prompt).strip()
            if not value:
                print(Fore.RED + "Input cannot be empty. Please enter a valid number.")
                continue
            return float(value)
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a numeric value.")

def calculator():
    while True:  
        try:
            print_gradient_text("""  
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗        ██╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╗╚██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    ╚═╝ ██║
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    ██╗ ██║
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    ╚═╝██╔╝
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝       ╚═╝
┏━━━━━━━━━━━━━━━━━━━━━━━┓
┃ owner -> Sakurapvp01  ┃              !  make the world a better place :)  !
┗━━━━━━━━━━━━━━━━━━━━━━━┛
            """)
            print()
            print(Fore.MAGENTA + "1. Basic operations: +, -, *, /")
            time.sleep(0.003)
            print()
            print(Fore.MAGENTA + "2. Percentages: '%'")
            time.sleep(0.003)
            print()
            print(Fore.MAGENTA + "3. Logarithm: 'log'")
            time.sleep(0.003)
            print()
            print(Fore.MAGENTA + "4. Square root: 'sqrt'")
            time.sleep(0.003)
            print()
            operation = input(Fore.MAGENTA + "Select an operation -> ").strip()
            if not operation:
                print(Fore.RED + "No operation selected. Please choose a valid option.")
                continue  

            if operation == '1':
                print()
                print(Fore.MAGENTA + "Basic operations: +, -, *, /")
                print()
                op = input(Fore.MAGENTA + "Select operation (+, -, *, /) -> ").strip()
                if op in ['+', '-', '*', '/']:
                    print()
                    num1 = get_float_input("Enter the first number -> ")
                    print()
                    num2 = get_float_input("Enter the second number -> ")
                    print()
                    if op == '+':
                        print(Fore.MAGENTA + f"Result: {num1 + num2}")
                    elif op == '-':
                        print(Fore.MAGENTA + f"Result: {num1 - num2}")
                    elif op == '*':
                        print(Fore.MAGENTA + f"Result: {num1 * num2}")
                    elif op == '/':
                        if num2 != 0:
                            print(Fore.MAGENTA + f"Result: {num1 / num2}")
                        else:
                            print(Fore.RED + "Error! Division by zero.")
                else:
                    print(Fore.RED + "Invalid operation selected.")
            
            elif operation == '2':
                print()
                num = get_float_input("Enter a number -> ")
                print()
                percent = get_float_input("Enter the percentage -> ")
                print()
                print(Fore.MAGENTA + f"{percent}% of {num} is {num * percent / 100}")
            
            elif operation == '3':
                num = get_float_input("Enter a number -> ")
                if num > 0:
                    print(Fore.MAGENTA + f"Logarithm of {num} is {math.log(num)}")
                else:
                    print(Fore.RED + "Error! Logarithm can only be calculated for positive numbers.")
            
            elif operation == '4':  
                num = get_float_input("Enter a number: ")
                if num >= 0:
                    print(Fore.MAGENTA + f"Square root of {num} is {math.sqrt(num)}")
                else:
                    print(Fore.RED + "Error! Square root of a negative number does not exist.")
            
            else:
                print(Fore.RED + "Unknown operation. Please select a valid one.")

        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()