#print formatting
print ('this is a string {}' .format ('INSERTED') )

print ('The {} {} {}' .format ('fox','quick','brown'))

print ('The {1} {2} {0}' .format ('fox','quick','brown'))

print ('The {q} {b} {f}' .format (f='fox',q='quick',b='brown'))

result = 100/777
print (result) 

#floating point 

print ('the result was {r:1.3f}'.format (r = result))

name = "Jose"
name1 = "Ryker"
name1age = 3
print ('Hello, his name is {}'.format (name))

#use f string instald of .format

print (f'Hello, his name is {name1} and he is {name1age} years old ')


