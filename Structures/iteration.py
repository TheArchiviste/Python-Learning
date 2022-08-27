for i in range(5):
    print(i)

for i in range(10, 21, 2):
    print(i)
else:
    print('Finished!')

list = [2, 3, 5, 7, 11, 13]
dict = {'name': 'Henry', 'age': 32, 'phone': '012345'}

for numbers in list:
    print(numbers)

for (key, value) in dict.items():
    print(f'{key} ----> {value}')

list2 = [1]

while len(list2) < 100:
    number = list2[len(list) - 1] * 2
    list2.append(number)

print(list2)