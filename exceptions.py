try:
    x = "3"
    y = 1
    result = x / y
except ZeroDivisionError:
    print('Operation failed due to division by zero.')
except Exception as exception:
    print(f'Operation failed: {exception}')
else:
    print(result)
finally:
    print('Finished!')


x = -1
if x <= 0:
    raise ValueError(f'x = {x} should have been a positive number.')
print('Do something with the value of x')