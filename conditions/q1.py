num_in = int(input("Enter a number: "))

num = num_in - 2
if num % 10 == 0:
    print("The number is 2 units away from a multiple of 10")
else:
    print("The number is not 2 units away from a multiple of 10")