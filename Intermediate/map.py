class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zack", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

student_results = [] #we need to create list first
for student in students:
    #if student.score >= 0.7:
        #student_results.append(f"{student.name} Passed") #add passed students to the list
    #else:
        #student_results.append(f"{student.name} failed") #add failed students to the list
    #To avoid above 4 lines we can do that in a single line which is showiing in the below line
    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} failed")

#map_results = list(map(lambda student: student.name, students))To disply only student name
map_results = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} failed", students)) #to again display both student name and result

print(map_results) #print the list
