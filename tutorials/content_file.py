try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File was not found")