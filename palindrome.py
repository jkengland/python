userword = input("Please type the word you would like to test.: ")
print(f'checking if the word "{userword}" is a palindrome')
reverseword = userword[::-1]
if userword == reverseword: print(f'"{userword}" is a palindrome')
else: print(f'"{userword}" is not a palindrome')