back = []
forward= []
current = "Home"

while True:
    print("\n1. Visit Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Current Location")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        place = input("Enter Place Name: ")

        back.append(current)
        current = place
        forward.clear()

        print("Current Location:", current)

    elif choice == 2:
        if back == []:
            print("No Previous Place")
        else:
            forward.append(current)
            current = back.pop()

            print("Current Location:", current)

    elif choice == 3:
        if forward == []:
            print("No Forward Place")
        else:
            back.append(current)
            current = forward.pop()

            print("Current Location:", current)

    elif choice == 4:
        print("Current Location:", current)

    elif choice == 5:
        print("End........!!!")
        break

    else:
        print("Invalid Choice")