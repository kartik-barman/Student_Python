#import os
#os.system('CLS')

#import subprocess
#subprocess.call("cls", shell=True)

print("********First Example of for Loop use*********")
for letter in 'Python':
   print(letter)
   

print("********Second Example of for Loop use********")
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:     
   print(fruit)
   
   
print("********Third Example of for Loop use********")
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6):
  print(x)

  
#range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 6):
  print(x)

print("********Fourth Example of for Loop use********")
for index in range(len(fruits)):
   print(fruits[index])   

#Increment the sequence with 3 (default is 1)
print("********Fifth Example of for Loop use********") 
for x in range(2, 30, 3):
  print(x)

#for Loop with else part
#Print all numbers from 0 to 5, and print a message when the loop has ended  
print("********Sixth Example of for Loop use********") 
for x in range(6):
  print(x)
else:
  print("Finally finished!")

