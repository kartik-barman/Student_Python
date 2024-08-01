#Tuple is ordered and unchangeable. Allows duplicate members
#Tuple items are indexed, the first item has index [0],second index [1] so on..

# Sort(),append(),insert(), pop() not applicable since unchangeable

T1 = ("apple", "banana", "cherry", "apple", "cherry")
T2 = ("abc", 34, True, 40,40, "male")  # max() and min() not applicable
T3 = ("xyz")  #not a tuple
T4=("xyz",)  # a tuple
T6={23,5,77,9,77,12,5} # max() and min() applicable
print(T1)

print("Print the type")
print(type(T1),type(T2),type(T3),type(T4))


print("Diplaying tuple in different way")
print(T2)
print("Diplaying tuple in a specified range")
print("T2[1:3]: ", T2[1:3])


print("Diplaying specified cell of a tuple")
print("T2[1]: ", T2[1])
print("Diplaying specified cell of a tuple with negative indexing")
print("T2[-1]: ", T2[-1])

print("Number of element in the tuple T1 is:")
print(len(T1))

print("Addition or Concatination of two Tuple:")
T5=T1+T2
print(T5)

print(max(T6))
print(min(T6))


      
