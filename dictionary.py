myCat = {'size': 'fat', 'color': 'gray','disposition': 'loud'}
myCat['size']
print ('My cat has ' + myCat['color'] + ' fur.')

eggs = {'name': 'Zophei', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophei', 'age': 8}
ham == eggs  #this willbe true because the dictionary has the same key values

list(eggs.keys())
