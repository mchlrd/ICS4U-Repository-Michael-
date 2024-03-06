counter = 0

for i in range(6):
    result = input(f"Enter the game {i+1} result: ")

if result == "W":
    counter = counter + 1

elif result == "L":
    pass

else:
    print("Enter a valid letter")


if counter > 4:
    print(1)

if counter > 2:
    print(1)

else:
    print(-1)