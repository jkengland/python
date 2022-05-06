myfile = open('myfile.txt')
myfile.readlines()
myfile.seek(0)
contents = myfile.read()
print ('hello')

#to open a file in a different location 
myfile = open ("C:\\python\\myfile.txt")

#close the file
myfile.close()

#to quickly edit a file 
with open('myfile.txt') as my_new_file:
    content = my_new_file.read()
contents
 
 #write to file
with open('myfile.txt',mode='r') as myfile:
    contents = myfile.read()
    
    
with open('myfile.txt',mode='r') as f:
   print(f.read())