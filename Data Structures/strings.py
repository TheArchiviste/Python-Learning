a = "Hello, World!"
b = 'Hello, World!'

# Compares the content stored in the object.
print(a == b)
# Checks whether the objects are the same.
print(a is b)

c = a
print(a is c)

print(a.upper())
print(a.lower())
print(a.find('World'))
print(a[7])
print(a[7:12])
print(len(a))
print(a[7:len(a)])

# F-strings
name = "Jonny"
age = 32

fstring = f'{name} is {age - 10} years old.'
print(fstring)