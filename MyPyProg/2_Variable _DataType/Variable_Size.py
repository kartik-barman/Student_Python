from sys import getsizeof  #this line is compulsory

a = 42
print(getsizeof(a))
a = 2**1000
print(getsizeof(a))


print(1e308) # 1 X 10 to the power 308
print(1e309)

print(1.7e308)  # 1.7 X 10 to the power 308
print(1.7e309)
