

print("   1. d4   2. d6    3. d8")
print("   4. d10  5. d12   6. d20  7. d100\n")

dice = int(input("what die would you like to roll "))
amount = int(input("number of dice:"))

if dice == 1:
  import random
  random_number = sum([random.randint(1,4) for i in range(amount)])
  print(random_number)  

if dice == 2:
  import random
  random_number = sum([random.randint(1,6) for i in range(amount)])
  print(random_number)  

if dice == 3:
  import random
  random_number = sum([random.randint(1,8) for i in range(amount)])
  print(random_number)  
     
if dice == 4:
  import random
  random_number = sum([random.randint(1,10) for i in range(amount)])
  print(random_number)  

if dice == 5:
  import random
  random_number = sum([random.randint(1,12) for i in range(amount)])
  print(random_number)  

if dice == 6:
  import random
  random_number = sum([random.randint(1,20) for i in range(amount)])
  print(random_number)           
         
if dice == 7:
  import random
  random_number = sum([random.randint(1,100) for i in range(amount)])
  print(random_number)       
