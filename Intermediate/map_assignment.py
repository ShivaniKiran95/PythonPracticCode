#Use map to multiply all these numbers by 2
# numbers = [1, 2, 3, 4, 5]

class Numbers:
    def __init__(self, numb):
        self.numb = numb

numbers = [Numbers("1") , Numbers("2") , Numbers("3") , Numbers("4") , Numbers("5")]

#number_result = []

#for number in numbers:

print(list(map(lambda number: int(number.numb)*2, numbers)))

#----------------------------------------------------

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*2, numbers)))
