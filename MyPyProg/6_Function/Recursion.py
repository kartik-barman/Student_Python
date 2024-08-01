def my_function(x):
  return 5 * x
print("Result of 1st call")
print(my_function(3))
print("Result of 2nd call")
print(my_function(5))
print("Result of 3rd call")
print(my_function(9))

""" O/P:
Result of 1st call
15
Result of 2nd call
25
Result of 3rd call
45  """
#__________________________________________
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

""" O/P:
apple
banana
cherry  """

#__________________________________________
def try_recursion(k):
  if(k > 0):
    result = k + try_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
try_recursion(6)

""" O/P:
Recursion Example Results
1
3
6
10
15
21   """
