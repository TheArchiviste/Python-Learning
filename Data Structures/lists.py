list = [1, 2, 'hello', 4.0, False]

print(list[2])
# Get all elements from index 2 to 4
print(list[2:4])

list[1] = 3
print(list[1])

list.append(6)
print(list)
# Remove the first occurence of the specified element
list.remove(4.0)
print(list)
list.insert(3, 8)
print(list)

list2 = list.copy()
print(list2 == list)
print(list2 is list)