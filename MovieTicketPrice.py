# Discounts
    # 6 or more people: 10% 
    # Is a member: 15% 

### English ###
# Ask user if they want to option 1 (create a booking)
# option 2 (add a movie), or option 3 (delete a movie) 
    # If user selects option 1, take user to create a booking
    # If user selects option 2, take user to add a movie to list
    # If user selects option 3, take user to delete a movie to list 

#### Create a booking ####

# Take user inputs (movie name, number of people, is a member or not)
# Find the movie price
    # Multiply the number of people and movie 
# Check if numPeople <= 6, if greater discount by 10% and add to finalTicketPrice
# Check if they are a member, if true discount by 15%, add to finalTicketPrice
# add saleTax to finalTicketPrice (9%)
# Print finalTicketPrice

#### Add a movie to list ####

# Take user input (movie name)
# add movie name to list of movies

#### Delete a movie to list #### 

# Take user input (movie name)
# delete movie from list of movies 


### Functions ###

import sys

def findMoviePriceByName(movieIndex, moviesList):
    if (movieIndex-1 >= 0) and (movieIndex-1 < len(moviesList)):
        return moviesList[movieIndex-1][1]  
    else:
        return None

def addDiscountByNumOfPeople(numPeople, price):
    if numPeople >= 6:
        price *= 0.9 
    return price

def addDiscountByMembership(price, isMemberPrompt):
    if isMemberPrompt == True: 
        price *= 0.85
    return price

def addSalesTax(price):
    return price*1.09

### Main Program ###
moviesList = []

while True: 
    print("------------------------------------------------------------")
    # read inputs
    print ("Option 1: Create a booking")
    print ("Option 2: Add a movie")
    print ("Option 3: Delete a movie")
    print ("Option 4: Quit Program \n")
    operation = int(input("Enter your choice: "))
    print()
    
    if operation == 1:
        print("The current movies playing are: ")
        listindex = 0
        while (listindex < len(moviesList)):
            print(f"{listindex+1}. {moviesList[listindex]}")
            listindex += 1

        movieNum = int(input("Enter the movie number: "))
        if movieNum > len(moviesList):
            print ("Please enter a valid input.")
            continue

        numPeople = int(input("Enter the number of people: "))
        if numPeople <= 0:
            print ("Please enter a valid input")
            continue
        
        isMemberPrompt = str(input("Are you a member (yes or no): ")).lower()
        if isMemberPrompt == "yes":
            isMemberPrompt = True
        elif isMemberPrompt == "no":
            isMemberPrompt = False
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
            continue

        # Get Movie Ticket Price by Movie Name
        moviePrice = findMoviePriceByName(movieNum, moviesList)

        # Caludate the bill for the group
        finalTicketPrice = numPeople * moviePrice

        # Apply eligible Discounts
        finalTicketPrice = addDiscountByNumOfPeople(numPeople, finalTicketPrice)
        finalTicketPrice = addDiscountByMembership(finalTicketPrice, isMemberPrompt)

        # Add Sales Tax 
        finalTicketPrice = addSalesTax(finalTicketPrice)

        # Print the Final price
        print ("Your ticket price is: ")
        print(round(finalTicketPrice, 2))
    elif operation == 2: 
        addMovieName = str(input("Enter a movie: "))
        addMoviePrice = int(input("Enter the price of the movie: "))
        movieList = (addMovieName, addMoviePrice)
        moviesList.append(movieList)
        print (f"The current movies are:")
        listindex = 0
        while (listindex < len(moviesList)):
            print(f"{listindex+1}. {moviesList[listindex]}")
            listindex += 1
    elif operation == 3:
        print (f"The current movies are:")
        listindex = 0
        while (listindex < len(moviesList)):
            print(f"{listindex+1}. {moviesList[listindex][0]}")
            listindex += 1
        if moviesList == []:
            print("There are no movies to delete")
            continue
        addMovieName = str(input("Enter the movie to be deleted: "))
        for moviePairs in moviesList:
            if moviePairs[0] == addMovieName: 
                moviesList.remove(moviePairs)
            else: 
                print ("Sorry. That movie does not exist")
                continue
        print("The current movies playing are: ")
        listindex = 0
        while (listindex < len(moviesList)):
            print(f"{listindex+1}. {moviesList[listindex][0]}")
            listindex += 1
    elif operation == 4: 
        print("Quitting program... \n")
        break
    else: 
        print ("Invalid Input. Please enter a valid input")
print("Have a nice day!")




### Testcases ###

# CASE 1
# Input: 

# people: 6 
# movie: 1 
# ismember: true
# salesTax = 9% 
# Ouput: $60.01

# CASE 2
# Input:
#  
# people: 4 
# movie: 3
# ismember: false
# salesTax = 9%
# Output: $43.6

# CASE 3
# Input: 
# 
# people: 1 
# movie: 2
# ismember: true
# salesTax = 9%   
# Output: $13.9

# CASE 5 
# Input: 
# 
# people: 
# movie: 
# ismember: 
# salesTax = 9% 
# Output: Error. Please enter a valid input(s)

# CASE 6
# Input: 
# 
# people: 7 
# movie: 3 
# ismember: 
# salesTax = 9% 
# Output: Errror. Please enter a valid input(s) 

#### TESTCASES 2 ####

# CASE 1
# Inputs: 
# 
# moviename: hello 
# Output: ['hello']

# CASE 2 
# Inputs:
# 
# deletemoviename: hello
# Output: []

# CASE 3 
# Inputs: 
# 
# moviename: 
# Output: []

# CASE 3 
# Inputs: 
#
# moviename: 3
# Output: Invalid Input 

#### TESTCASES 3 ####

# CASE 1 
# Inputs: 
#
# moviename (only 3): 5
# Output: Invalid Input 