from functools import reduce
number = 1234

sum_of_digits = reduce(lambda x, y: int(x) + int(y), str(number))
print(sum_of_digits)