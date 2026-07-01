back_stack = []
forward_stack = []
current = "Home"

def visit(place):
    global current

    back_stack.append(current)
    current = place
    forward_stack.clear()

    print("Current Location :", current)


def back():
    global current

    if len(back_stack) == 0:
        print("No Previous Place")
    else:
        forward_stack.append(current)
        current = back_stack.pop()
        print("Current Location :", current)


def forward():
    global current

    if len(forward_stack) == 0:
        print("No Forward Place")
    else:
        back_stack.append(current)
        current = forward_stack.pop()
        print("Current Location :", current)


while True:

    print("\n------ MENU ------")
    print("1. Visit Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Current Location")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        place = input("Enter Place Name: ")
        visit(place)

    elif choice == 2:
        back()

    elif choice == 3:
        forward()

    elif choice == 4:
        print("Current Location :", current)

    elif choice == 5:
        print("Program End")
        break

    else:
        print("Invalid Choice")