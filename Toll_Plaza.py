queue=[]
size=5

while True:
    print("1. Insert Vehicle")
    print("2. Remove Vehicle")
    print("3. Display Queue")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch==1:
        if len(queue)==size:
            print("Queue Is Full")
        else:
            vehicle=input("Enter Vehicle Name :- ")
            queue.append(vehicle)
            print("Vehicle Added Successfully")   
    elif ch==2:
        if len(queue)==0:
            print("Queue Is Empty")
        else:
            print("Vehicle Removed Successfully")
            queue.pop(0)     
    elif ch==3:
        if len(queue)==0:
            print("Queue Is Empty")
        else:
            print("Vehicle In Queue")
            for vehicle in queue:
                print(vehicle)
    elif ch==4:
        break 
    else:
        print("Invalid Choice") 
    