cars = ["Ford", "Volvo", "BMW"]
print("Main Array....")
for x in cars:
  print(x)
  
x = cars[0]
print(x)

cars[0] = "Toyota"
x = len(cars)
print(x,sep='\n')

cars.append("Honda")
print('Array after appending Volvo....')
for x in cars:
  print(x)

print(cars.pop(2))

cars.remove("Volvo")
print('Array after removing Volvo....')
for x in cars:
  print(x)
