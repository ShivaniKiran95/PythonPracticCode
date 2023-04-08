import pickle

class ToDo:
    def __init__(self, title, important, category = "Normal"):
        self.title = title
        self.important = important
        self.category = category

todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category = "Work")]

age = [28,22,30,3,45,33,54]

file = open("text.txt", "wb") #w=overwrite a file b=writing binary data
pickle.dump(todos, file)
file.close()


file = open("text.txt", "rb") #rb=read binary data
new_todos = pickle.load(file)
file.close()

print(new_todos)
