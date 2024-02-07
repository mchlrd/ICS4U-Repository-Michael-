capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')

#print(capitals.get('Germany'))
#(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key, value)