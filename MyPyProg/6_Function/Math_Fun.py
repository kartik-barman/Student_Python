
#Built-in Math Functions
#To use it, you must import the math module

import math

print("The min() and max() functions to find the lowest or highest value")

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


print("The abs() function returns the absolute (positive) value")

x = abs(-7.25)
print(x)

print("The pow(x, y) function returns the value of x to the power y")

x = pow(4, 3)
print(x)

print("The math.sqrt() method for example, returns the square root of a number")

x = math.sqrt(64)
print(x)

print("The math.ceil() method rounds a number upwards to its nearest integer")
print("The math.floor() method rounds a number downwards to its nearest integer")
x = math.ceil(1.4)   
y = math.floor(1.4)  

print(x) # returns 2
print(y) # returns 1


print("The math.pi constant, returns the value of PI (3.14...)")

x = math.pi
print(x)
