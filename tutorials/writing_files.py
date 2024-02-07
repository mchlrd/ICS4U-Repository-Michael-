text = "Hey\nThis is a text\nHave a nice day\n"

with open('test1.txt', 'w') as file:
    file.write(text)

with open('test1.txt') as file:
    print(file.read())