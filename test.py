#timestoprint = int(input("How many times to print hello?"))
#if timestoprint == 2:
#    for i in range(timestoprint):
#        print("hello")
#    
    
#import random
#random_number = random.randint(1,4)
#
#print(random_number * 4 )


import random
random_number = sum([random.randint(1,4) for i in range(25)])
print(random_number)