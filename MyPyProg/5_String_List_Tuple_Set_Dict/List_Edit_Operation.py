# Python3 program for explaining use of lists

L1 = [2,55,14,100]
L2 = [44,5,34,22]
L3 = []

# Adding Element into list (Always add in last)
L1.append(5)
L1.append(10)
print("Adding 5 and 10 in list", L1)

# Popping Elements from list (Always pop from last)
L1.pop()
print("Popped one element from list", L1)
print()

# Removing Elements from list (any Element from list)
L2.remove(34)
print("Element 34 removed from list", L2)
print()

# Insertinging Elements to list (any Element in a specified index in list)
L2.insert(0,54)
print("Element 54 inserted in index no 0 list", L2)
print()

# Sortinging Elements in a list 
L2.sort()
print("Elements after sorting the list L2", L2)
print()

# Adding Elements for two list
L3=L1+L2
print("Elements after Adding L1 and L2 into list L3", L3)
print()

# Clearing Elements from a list
L3.clear()
print("Printing L3 after clearing", L3)
print()

# Deleting a list (Removing Memory from RAM) 
del L1
# print() name 'L1' is not defined. 



