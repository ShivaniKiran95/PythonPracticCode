        #Read
#file = open("cheese.txt", "r")
#lines = file.readlines()
#file.close()

        #Edit (to edit whole file)
#lines = ["Hello\n", "My name is Shivani Kiran!!"]

        #Edit(to add line or strings to the initial file)
#lines.insert(0, "I Hate Cheese\n")

        #Edit(to replace the perticular line in a file)
#lines[1] = "Hello Friends!\n"

        #Edit(add a line in a very end of a txt file)
#lines[-1] = lines[-1] + "\n"
#lines.append("Goodbye!")


        #Write
#file = open("cheese.txt", "w")
#file.writelines(lines)
#file.close()

#Challenge
#Multiply each of the number in numbers.txt by 2
file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

for x in range(len(lines)):

    try:
        number = float(lines[x]) *2
        lines[x] =f"{number}\n"
    except Exception as e:
        pass

file = open("numbers.txt", "w")
file.writelines(lines)
file.close()
