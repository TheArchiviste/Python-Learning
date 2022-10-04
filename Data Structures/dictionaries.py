dict = {'name': 'Jonny', 'age': 32}

print(dict['name'])
print(dict['age'])
# The keys are usually strings, but it can be otherwise.

dict['age'] = 85
print(dict['age'])

dict['age'] += 1
print(dict['age'])
print(dict.keys())

# Turns the dictionary into a list of tuples.
print(dict.items())
