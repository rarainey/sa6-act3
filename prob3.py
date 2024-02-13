from functools import reduce
numbers = [2, 1, 8, 41, 5, 7, 6, 10, 9]

maximum = reduce(lambda x, y: x if x>y else y, numbers)
print(maximum)