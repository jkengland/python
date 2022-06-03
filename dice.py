

print("   1. d4   2. d6    3. d8")
print("   4. d10  5. d12   6. d20  7. d100\n")

dice = int(input("what die would you like to roll "))
amount = int(input("number of dice:"))
answer = ""

if dice == 1:

 for i in range(amount):
  import random
  random_number = random.randint(1,4)
  print(random_number)  
     
    


#if random_number == 1:
#      answer = "Yes - definitely."
#elif random_number == 2:11
#  answer = "It is decidedly so."
#elif random_number == 3:
#  answer = "Without a doubt."
#elif random_number == 4:
#  answer = "Reply hazy, try again."
#elif random_number == 5:
#  answer = "Ask again later."
#elif random_number == 6:
#  answer = "Better not tell you now."
#elif random_number == 7:
#  answer = "My sources say no."
#elif random_number == 8:
#  answer = "Outlook not so good."
#elif random_number == 9:
#  answer = "Very doubtful."
#elif random_number == 10:
#  answer = "Yes"
#else:
#  answer = "Error"
#print(name, "asks:", question)
#print("Magic 8-Ball's answer:",answer)