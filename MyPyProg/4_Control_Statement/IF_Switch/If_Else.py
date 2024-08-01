#if:--else Statement
age = 18
if ((age>= 8) and (age<= 12)):
	print("YOU ARE ALLOWED. WELCOME !")
else:
	print("SORRY ! YOU ARE NOT ALLOWED. BYE !")

# if:--elif: Example

var = 'N'

if (var =='Y' or var =='y'):
	print("YOU SAID YES")
elif(var =='N' or var =='n'):
	print("YOU SAID NO")
else:
	print("INVALID INPUT")
	
#  O/P:YOU SAID NO
	
# IF with multiple condition
a = 7
b = 9
c = 3
if((a>b and a>c) and (a != b and a != c)):
	print(a, " is the largest")
elif((b>a and b>c) and (b != a and b != c)):
	print(b, " is the largest")
elif((c>a and c>b) and (c != a and c != b)):
	print(c, " is the largest")
else:
	print("entered numbers are equal")

#  O/P: 9  is the largest

#Nested IF
num = int(input("enter number :"))
if num%2 == 0:
   if num%3 == 0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3 == 0:
      print ("divisible by 3 not divisible by 2")
   else:
      print  ("not Divisible by 2 not divisible by 3")
      

# "all" OR "any" NOT REQUIRED IN DIPLOMA LEVEL

# Checking For Multiple Conditions to be True in Python if-else Statements
age = 32

if all([age >= 0,  age < 20]):
    group = "0-19"
elif all([age >= 20, age < 30]):
    group = "20-29"
else:
    group = "30+"

print(f'Person is in group: {group}')

# O/P: Person is in group: 30+

# Checking For Some Conditions to be True in Python if-else Statements
weekday = 'Friday'

if weekday == 'Saturday' or weekday == 'Sunday':
    print("Yay! It's the weekend!")
else:
    print("Time to go to work.")

# O/P: Time to go to work.

# Checking For Some Conditions to be True in Python if-else Statements
weekday = 'Friday'

if any([weekday == 'Saturday', weekday == 'Sunday']):
    print("Yay! It's the weekend!")
else:
    print("Time to go to work.")

# O/P: Time to go to work.
