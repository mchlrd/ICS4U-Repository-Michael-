telenum = []
for i in range(4):
    i = int(input("Enter the last four digits of the telephone number: "))
    telenum.append(i)

if telenum[0] == 8 or telenum[0] == 9 and telenum[3] == 8 or telenum[3] == 9 and telenum[1] == telenum[2]:
    print("ignore")
else:
    print("answer")

