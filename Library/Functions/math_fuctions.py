def average(number, *args):
    sum = number
    count = 1
    for value in args:
        sum += value
        count += 1
    return sum/count