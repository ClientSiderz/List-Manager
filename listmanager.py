import os
import sys
import json
import platform
import subprocess

required_modules = ['colored', 'pyfiglet']

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

from colored import fore, back, style
from pyfiglet import Figlet

def clear_terminal():
    """Clears the terminal screen."""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def load_session():
    """Loads the session data from a file."""
    try:
        with open(".listmanager/session.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{fore('red')}Error: Last session not found. A new session file will be made when exited.{style('reset')}")
        return []

def save_session(data):
    """Saves the session data to a file."""
    os.makedirs(".listmanager", exist_ok=True)
    with open(".listmanager/session.json", "w") as file:
        json.dump(data, file)

def add_number(numbers):
    """Adds a number to the list."""
    clear_terminal()
    number = int(input("Enter a number to add to the list: "))
    numbers.append(number)

def remove_number(numbers):
    """Removes a number from the list."""
    clear_terminal()
    if not numbers:
        print(f"{back('red')}Operation failed, the list is empty.{style('reset')}")
        return

    print("Select which number to remove by entering their count:")
    for i, n in enumerate(numbers):
        print(f"{i + 1} - {n}")
    try:
        index = int(input("> ")) - 1
        numbers.pop(index)
    except (IndexError, ValueError):
        clear_terminal()
        print(f"{back('red')}Invalid input. Please enter a valid number.{style('reset')}")

def manage_number(numbers):
    """Performs mathematical operations on a number in the list."""
    clear_terminal()
    if not numbers:
        print(f"{back('red')}Operation failed, the list is empty.{style('reset')}")
        return

    print("Which number would you like to manage?")
    for i, n in enumerate(numbers):
        print(f"{i + 1} - {n}")
    try:
        index = int(input("> ")) - 1
        number = numbers[index]

        print("Which mathematical operation would you like to do?")
        operation = int(input("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n> "))

        match operation:
            case 1:
                clear_terminal()
                add = int(input("Enter a number to add to the selected number: "))
                number += add
            case 2:
                clear_terminal()
                sub = int(input("Enter a number to subtract from the selected number: "))
                number -= sub
            case 3:
                clear_terminal()
                mul = int(input("Enter a number to multiply the selected number by: "))
                number *= mul
            case 4:
                clear_terminal()
                div = int(input("Enter a number to divide the selected number by: "))
                if div == 0:
                    print(f"{back('red')}Cannot divide by zero.{style('reset')}")
                else:
                    number /= div
            case _:
                clear_terminal()
                print(f"{back('red')}Invalid input. Please enter a valid number.{style('reset')}")

    except (IndexError, ValueError):
        clear_terminal()
        print(f"{back('red')}Invalid input. Please enter a valid number.{style('reset')}")

if __name__ == "__main__":
    numbers = load_session()

    while True:
        f = Figlet(font="slant")
        
        print(f'{fore('dark_green')}{f.renderText("List Manager")}{style('reset')}')
        print(f'{fore('dark_goldenrod')}Current List{fore('light_gray')}: {fore('white')}{numbers}{style('reset')}')
        print('''
1 - Add a number
2 - Remove a number
3 - Manage numbers in the list
4 - Sort the list
5 - Clear the list
6 - Exit
        ''')
        try:
            choice = int(input("> "))
            match choice:
                case 1:
                    add_number(numbers)
                case 2:
                    remove_number(numbers)
                case 3:
                    manage_number(numbers)
                case 4:
                    clear_terminal()
                    numbers.sort()
                case 5:
                    clear_terminal()
                    numbers.clear()
                case 6:
                    save_session(numbers)
                    print("Goodbye!")
                    break
                case _:
                    clear_terminal()
                    print(f"{back('red')}Invalid input. Please enter a valid number.{style('reset')}")
        except ValueError:
            clear_terminal()
            print(f"{back('red')}Invalid input. Please enter a valid number.{style('reset')}")