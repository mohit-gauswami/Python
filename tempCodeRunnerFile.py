    elif ch==4:
        slot=int(input("Enter Slot Number (0-7) :- "))
        new_product=input("Enter New Product Name :- ")

        if belt[slot] !=None:
            belt[slot]=new_product
            print(f"Product Update Successfully.")
        else:
            print("Slot Empty")

    elif ch==5:
        if None not in belt:
            print("Belt is full.")
        else:
            print("Belt is not full.")       

    elif ch==6:
        print(belt)

    elif ch==7:
        break

    else:
        print("Invalid Choice.")