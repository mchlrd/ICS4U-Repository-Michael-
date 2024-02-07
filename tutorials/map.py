store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jackets", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]* 0.82)
to_usd = lambda data: (data[0], data[1]/0.82)

store_euros = list(map(to_euros, store))
store_usd = list(map(to_usd, store))

for i in store_euros:
    print(i)

print(" ")

for i in store_usd:
    print(i)