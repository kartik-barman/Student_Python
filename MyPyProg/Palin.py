str = input("Enter a String:") 

#
#strstr = str.casefold()  
  
# This string is reverse.  
rev = reversed(str)  
  
if list(str) == list(rev):  
   print("PALINDROME !")  
else:  
   print("NOT PALINDROME !")  


#---------- Number Palindrome Check .......

num = int(input("Enter a value:"))  
temp = num  
rev = 0  
while(num > 0):  
    dig = num % 10  
    rev = rev * 10 + dig  
    num = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  
