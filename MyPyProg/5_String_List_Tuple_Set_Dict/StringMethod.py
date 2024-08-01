a = "      Hello, World!      "

# The upper() method returns the string in upper case
print(a.upper())

# The lower() method returns the string in lower case
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end
print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.
txt = "Company10"
x = txt.isalpha()
print(x)

# Returns True if all characters in the string are alphanumeric
x = txt.isalnum()
print("isalnum() Check:", x)

# Returns True if all characters in the string are digits
txt="12345"
x = txt.isdigit()
print("isdigit() Check:", x)



