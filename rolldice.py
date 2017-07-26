import random

# This is a simple dice rolling game that exits on any other input that is not y
while True:
    userIn = input("Would you like to roll the dice?")

    if userIn == "y":
        print(random.randint(1,12))

    else:
        break
