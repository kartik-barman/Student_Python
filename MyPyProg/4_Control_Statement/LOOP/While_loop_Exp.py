# Different use of While Loop


print("1st Example of While LOOP")
i = 1
while i < 6:
  print(i)
  i += 1


print("2nd Example of While LOOP with BREAK Statement")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


print("3rd Example of While LOOP with CONTINUE statement")
i = 1
while i < 6:
  if i == 3:
    continue
  print(i)
  i += 1

print("4th Example of While LOOP")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
