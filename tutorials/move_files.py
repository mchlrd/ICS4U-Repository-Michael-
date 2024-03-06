import os

source = "test1.txt"
destination = "C:\\Users\\Michael\\Desktop\\test1.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print("The file was moved")
except FileNotFoundError:
    print(source+" Was not Found")