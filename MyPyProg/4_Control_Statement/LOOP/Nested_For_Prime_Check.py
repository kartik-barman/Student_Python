#Nested for Loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x,y)

# Prime number Check

for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, of the first FOR
   else:                  # else part of the loop
         print(num,'is a prime number')
	    
