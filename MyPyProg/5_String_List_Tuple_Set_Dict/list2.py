thislist = ["apple", "banana", "cherry"]
thistuple = ["kiwi", "orange"]
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ["kiwi", "orange"]
thislist=thislist+thistuple
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist=thislist+thistuple # Not Possible
print(thislist)
