list = []

print('List Manager')
print(f"Current List: {list}")

def starterMenu():
    print('''
Add a number - 1
Remove a number - 2
Sort the list - 3
Manage one of the numbers - 4
''')
    startChoice = int(input("> "))
    if(startChoice == 1):
        addNumber()
    elif(startChoice == 2):
        if len(list) > 0:
            removeNumber()
        else:
            print("Operation failed, the list is empty")
            starterMenu()
    elif(startChoice == 3):
        list.sort()
        print(f"Current List: {list}")
        starterMenu()
    elif(startChoice == 4):
        print("Manage")
    else:
        print("Invalid choice. Please try again.")
        starterMenu()
        
def addNumber():
    print("Enter a number to add to the list: ")
    
    number = int(input("> "))
    list.append(number)
    
    print(f"Current List: {list}")
    starterMenu()
    
def removeNumber():
    print("Select which number to remove by entering their count: ")
    
    for n in list:
        print(f"{list.index(n) + 1} - {n}")
        
    number = int(input("> "))
    list.remove(list[(number - 1)])
    
    print(f"Current List: {list}")
    starterMenu()

starterMenu()