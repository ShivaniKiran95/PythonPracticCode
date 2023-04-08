import sys

#for argument in sys.argv:
    #print(argument)


#make a script that multiplies all the number arguments passed into it:
total = 1
del(sys.argv[0])
for argument in sys.argv:

    try:
        number = int(argument)
        total *= number
    except Exception as e:
        print(e)
        print("Only numbers can be provided")
        sys.exit(1)

print(total)
