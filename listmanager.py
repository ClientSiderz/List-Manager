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
    print("Select which number to remove by entering their count: ")
    
    for n in list:
        print(f"{list.index(n) + 1} - {n}")
        
    number = int(input("> "))
    list.remove(list[(number - 1)])
    
    clearTerminal()
    
# Number Management Functions

def manageList():
    print("Which number would you like to manage?")
    

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
                clearTerminal()
                
                manageList()
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