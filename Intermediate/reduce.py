class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"



students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zack", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

score_total = 0

for student in students:
    score_total += student.score
#print(score_total)
#print(score_total/len(students))#avarage score

from functools import reduce

reduce_total = reduce(lambda total, x: x.score + total, students, 0)

#print(reduce_total) #total
print(round(reduce_total / len(students), 2)) #average
