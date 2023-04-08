#file = open("cheese.txt", "r")

       #read a file
#file_txt = file.read()
#print(file_txt)

       #read a file is by getting all the lines from file & putting that into a list
#lines =  file.readlines()
#print(lines)

      #here file reads it line by line.
#for line in file:
    #print(line)

#file.close()


#challenge
#create a file number.txt that has a few lines of numbers.
#Multiply all the numbers together and print the result.

file = open("numbers.txt", "r")

total = 1
for line in file:
    try:
        number = float(line)
        total *= number
    except Exception as e:
        pass

print(total)        

file.close()
