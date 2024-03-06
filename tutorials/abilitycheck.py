from random import randrange

dice_roll = randrange(1,21)

print(f"You rolled {dice_roll}.")

difficulty = int(input("Set a difficulty: "))


if dice_roll >= difficulty:
    print("Successful")
else:
    print("Unsuccessful")

