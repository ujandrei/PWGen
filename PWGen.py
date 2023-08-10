import random
from randomChar import *

print("How many characters? < 100")

length = input("> ")

while not length.replace('.', '', 1).isdigit():
    print("How many characters?")
    length = input("> ")

length = int(length)    
        
print("Do you want to add capital letters? (Y/N)")
CapitalsChoice = input(">")

while CapitalsChoice != "Y" and CapitalsChoice != "y" and CapitalsChoice != "N" and CapitalsChoice != "n":
    print("Do you want to add special characters? (Y/N)")
    CapitalsChoice = input(">")

if CapitalsChoice == "Y" or CapitalsChoice == "y":
    CapitalsChoice = True

else:
    CapitalsChoice = False


print("Do you want to add special characters? (Y/N)")
specialChar = input(">")

while specialChar != "Y" and specialChar != "y" and specialChar != "N" and specialChar != "n":
    print("Do you want to add special characters? (Y/N)")
    specialChar = input(">")

if specialChar == "Y" or specialChar== "y":
    specialChar = True

else:
    specialChar = False

print("Do you want to add numbers? [Y/N]")
NumbersChoice = input("> ")

while NumbersChoice != "Y" and NumbersChoice != "y" and NumbersChoice != "N" and NumbersChoice != "n":
    print("Do you want to add special characters? (Y/N)")
    NumbersChoice = input(">")

if NumbersChoice == "Y" or NumbersChoice == "y":
    NumbersChoice = True

else:
    NumbersChoice = False

trueCounter = 1 #begins with 1, its assumed you always want lowercase letters


if CapitalsChoice == True:
    trueCounter += 1

if specialChar == True:
    trueCounter += 1

if NumbersChoice == True:
    trueCounter += 1

randomQuantity = length / trueCounter + 1
randomQuantity = int(randomQuantity)

capitals = []
specials = []
numbers = []

Randomizer = randomChar()

lowercase = Randomizer.lowercaseRandomizer(randomQuantity)

if CapitalsChoice == True:
    capitals = Randomizer.CapitalRandomizer(randomQuantity)

if specialChar == True:
    specials = Randomizer.SpecialRandomizer(randomQuantity)

if NumbersChoice == True:
    numbers = Randomizer.NumberRandomizer(randomQuantity)

numbers = [str(num) for num in numbers] #converte os números inteiros em string nesta lista, de forma a poder adicioná-los enquanto string posteriormente.

sumLists = lowercase + capitals + specials + numbers
randomList = random.sample(sumLists, length)

print(randomList)
finalString = ''.join(randomList)
print(finalString)





















