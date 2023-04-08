#creating file("x") -> Creates only if the file doesn't exist

"""file= open("cheese.txt", "x")

file.write("X marks the spot!")

file.close()

#Overwrite file("w") ->

file= open("cheese.txt", "w")

file.write("for the W!")

file.close()

#Append("a")

file= open("cheese.txt", "a")

file.write("A+ work!")

file.close()"""

#Create a file named after an argument passed to the script.

import sys

file_name = sys.argv[1]
file = open(file_name, "w")
file.close()
