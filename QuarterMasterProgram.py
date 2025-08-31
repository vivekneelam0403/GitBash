# English
# Show backPack
    # if user chooses option 1, print backPack
# Create item 
    # if user chooses option 2, ask user: "Enter the item you want to add to the backpack:"
    # Append user input to backPack
# Delete item 
    # if user chooses option 3, print backPack and ask user: "Enter the item you want to delete
    # from the backpack"
    # Remove user input from backPack
# Quit Program
    # if user chooses option 4, then exit program

### Program ###

print("(1) Show Backpack")
print("(2) Create Item")
print("(3) Delete Item")
print("(4) Quit Program")
print()

backPack = []
operation = int(input("Enter your choice: "))
print()

while True:
    if operation == 1: 
        print("Showing your BackPack...")
        if backPack == []:
            print("There are no items in the BackPack")
            continue
        else:
            print("Your items are: ")
            listindex = 0
            while (listindex < len(backPack)):
                print(f"{listindex+1}. {backPack[listindex]}")
            listindex += 1
    elif operation == 2: 
        item = str(input("Enter the item you want to add: "))
        backPack.append(item)
    elif operation == 3: 
        if backPack == []:
            print("There is nothing in your BackPack")
            continue
        else:
            item = str(input("Enter the item you want to delete: "))
            backPack.remove(item)
    elif operation == 4: 
        print("Quitting program...")
        break 
    else: 
        print("Invalid Input. Please enter a valid input")

print("Have a nice day!")



