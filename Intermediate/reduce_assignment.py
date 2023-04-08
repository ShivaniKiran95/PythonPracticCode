#Use reduce to multiply all the number together.

numbers = [1, 2, 3, 4, 5]

from functools import reduce

mult_numb = reduce(lambda total, x: x*total, numbers, 1)
print(mult_numb)
