def is_it_true(expression):
    if expression:
        print(f'{expression} evaluates as True')
    else:
        print(f'{expression} evaluates as False')

is_it_true(True)
is_it_true(0)
is_it_true(1)
is_it_true(0.2)
is_it_true([])
is_it_true([0])
is_it_true(None)
is_it_true('')
is_it_true('0')

def average(a, b):
    return (a+b)/2

def average2(*args):
    sum = 0
    count = 0
    for value in args:
        sum += value
        count += 1
    return sum/count

def average3(number, *args):
    sum = number
    count = 0
    for value in args:
        sum += value
        count += 1
    return sum/count

print(f'The average of 5 and 7 is {average(5,7)}')
print(f'The average of 5 and 7 is {average2(5,7)}')
print(f'The average of 11 is {average2(11)}')
print(f'The average of 5, 7, 9 is {average2(5,7,9)}')
print(f'The average of 5 and 7 is {average3(5,7)}')

def power(base, exponent):
    return base ** exponent

print(f'2 ** 3 equals {power(2,3)}')
print(f'2 ** 3 equals {power(base = 2, exponent = 3)}')
print(f'2 ** 3 equals {power(exponent = 3, base = 2)}')

def print_kwargs(**kwargs):
    for (key, value) in kwargs.items():
        print(f'{key} ----> {value}')

def print_kwargs2(banned = False, **kwargs):
    kwargs['banned'] = banned
    for (key, value) in kwargs.items():
        print(f'{key} ----> {value}')

print_kwargs(name='Jonny', age=32, phone='87834243')
print_kwargs2(name='Jonny', age=32, phone='87834243')
print_kwargs2(name='Jenny', age=32, phone='87834243', banned=True)