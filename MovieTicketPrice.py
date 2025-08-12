# Discounts
    # 6 or more people: 10% 
    # Is a member: 15% 

### English ###

# Take user inputs (movie name, number of people, is a member or not)
# Find the movie price
    # Multiply the number of people and movie 
# Check if numPeople <= 6, if greater discount by 10% and add to finalTicketPrice
# Check if they are a member, if true discount by 15%, add to finalTicketPrice
# add saleTax to finalTicketPrice (9%)
# Print finalTicketPrice

### Functions ###

import sys


def findMoviePriceByName(movie):
    if movie == 1: 
        moviePrice = 12 
    elif movie == 2: 
        moviePrice = 15
    elif movie == 3: 
        moviePrice = 10
    elif movie == 4: 
        moviePrice = 12
    else: 
        print("Please enter a valid movie")
        moviePrice = 0 
    return moviePrice

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
while True: 
    print("------------------------------------------------------------")
    # read inputs
    movie = int(input("Enter the movie # (1,2,3,4): "))
    if movie not in range(1, 5):
        print("Invalid input. Please enter a valid movie number (1-4).")
        continue

    numPeople = int(input("Enter the number of people: "))
    isMemberPrompt = str(input("Are you a member. Enter true or false: ")).lower()

    # Input validations
    if isMemberPrompt == "true":
        isMemberPrompt = True
    elif isMemberPrompt == "false":
        isMemberPrompt = False
    else:
        print("Invalid input. Please enter 'True' or 'False'.")
        continue

    # Get Movie Ticket Price by Movie Name
    moviePrice = findMoviePriceByName(movie)

    # Caludate the bill for the group
    finalTicketPrice = numPeople * moviePrice

    # Apply eligible Discounts
    finalTicketPrice = addDiscountByNumOfPeople(numPeople, finalTicketPrice)
    finalTicketPrice = addDiscountByMembership(finalTicketPrice, isMemberPrompt)

    # Add Sales Tax 
    finalTicketPrice = addSalesTax(finalTicketPrice)

    # Print the Final price
    print(round(finalTicketPrice, 2))



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