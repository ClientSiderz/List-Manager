import os
import platform

list = []

#List Managment Functions
        
def addNumber():
    print("Enter a number to add to the list: ")
    
    number = int(input("> "))
    list.append(number)
    
    clearTerminal()
    
def removeNumber():
    try:
        clearTerminal()
                
        print("Select which number to remove by entering their count: ")
        
        for n in list:
            print(f"{list.index(n) + 1} - {n}")
            
        number = int(input("> "))
        list.remove(list[(number - 1)])
        
    except IndexError:
        clearTerminal()
        print("Invalid input, Please enter a valid number.")
    
# Number Management Functions

def manageListNumber():
    try:
        clearTerminal()
        
        print("Which number would you like to manage?")
        
        for n in list:
            print(f"{list.index(n) + 1} - {n}")
            
        number = int(input("> "))
        
        print("Which mathematical operation would you like to do?")
        
        operation = int(input("1 - Addition\n2 - Subtract\n3 - Multiply\n4 - Divide\n> "))
        
        match operation:
            case 1:
                clearTerminal()
                
                print("Enter a number to add to the selected number: ")
                
                add = int(input("> "))
                list[(number - 1)] += add
            case 2:
                clearTerminal()
                
                print("Enter a number to subtract to the selected number: ")
                
                sub = int(input("> "))
                list[(number - 1)] -= sub
            case 3:
                clearTerminal()
                
                print("Enter a number to multiply to the selected number: ")
                
                mul = int(input("> "))
                list[(number - 1)] *= mul
            case 4:
                clearTerminal()
                
                print("Enter a number to divide to the selected number: ")
                
                div = int(input("> "))
                list[(number - 1)] /= div
            case _:
                clearTerminal()
                print("Invalid input, Please enter a valid")
                    
    except IndexError:
        clearTerminal()
        print("Invalid input, Please enter a valid number.")
    

# Utility Functions

def clearTerminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# While loop to keep the program running until the user decides to exit

while True:
    print('------------------')
    print('List Manager')
    print('------------------')
    print(f"Current List: {list}")
    print('''
1 - Add a number
2 - Remove a number
3 - Manage numbers in the list
4 - Sort the list
5 - Exit
    ''')
    try:
        choice = int(input("> "))
        match choice:
            case 1:
                addNumber()
            case 2:
                if len(list) > 0:
                    removeNumber()
                else:
                    print("Operation failed, the list is empty")
            case 3:
                if len(list) > 0:
                    manageListNumber()
                else:
                    print("Operation failed, the list is empty")
            case 4:
                clearTerminal()
                
                list.sort()
            case 5:
                print("Goodbye!")
                break
            case _:
                clearTerminal()
    except ValueError:
        clearTerminal()
        print("Invalid input, Please enter a valid number.")