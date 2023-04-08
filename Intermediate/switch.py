"""direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")

    case "south":
        print("Down")

    case "east":
        print("Left")

    case "west":
        print("Right")

    case _:
        print("Not a valid direction")"""

#Assignment:
menu_number = input("What you want to order? ").lower()

match menu_number:
    case "1":
        print("Tomato Soup")

    case "2":
        print("Grill Cheese")

    case "3":
        print("Biriyani")

    case "4":
        print("Pepper Chicken")

    case _:
        print("Invalid Number")
