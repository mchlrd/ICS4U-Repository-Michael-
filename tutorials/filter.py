friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data: data[1] >= 18

drinking_friends = list(filter(age, friends))

for i in drinking_friends:
    print(i)