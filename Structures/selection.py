import numbers


number = -16

if number < 0:
    print(f'{number} is negative.')
elif number % 2 == 0:
    print(f'{number} is even.')
else:
    print(f'{number} is odd.')