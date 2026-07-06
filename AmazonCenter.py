belt= [None]*8

while True:
    print("1. Add Product")
    print("2. Check Slot")
    print("3. Find Product")
    print("4. Update Product")
    print("5. Check Belt Full")
    print("6. Display Belt")
    print("7. Exit")

    ch= int(input("Enter Your Choice :- "))

    if ch==1:
        slot=int(input("Enter Slot Number (0-7) :- "))
        product=input("Enter Product Name :- ")

        if slot >= 0 and slot < 8:
            if belt[slot] is None:
                belt[slot]=product
                print(f"Product {product} added to slot {slot}.")
            else:
                print(f"Slot {slot} is already occupied.")
    elif ch==2:
        slot=int(input("Enter Slot Number (0-7) :- "))

        if belt[slot]==None:
            print(f"Slot {slot} is empty.")
        else:
            print(f"Product : {belt[slot]}")

    elif ch==3:
        product=input("ENter Product Name :- ")

        if product in belt:
            print(f"Product {product} is found.")
        else:
            print(f"Product {product} is not found.")

    elif ch==4:
        slot=int(input("Enter Slot Number (0-7) :- "))
        new_product=input("Enter New Product Name :- ")

        if belt[slot] !=None:
            belt[slot]=new_product
            print(f"Product Update Successfully......")
        else:
            print("Slot Empty")

    elif ch==5:
        if None not in belt:
            print("Belt is full")
        else:
            print("Belt is not full")       

    elif ch==6:
        print(belt)

    elif ch==7:
        break

    else:
        print("Invalid Choice.")