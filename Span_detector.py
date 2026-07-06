blacklist = ["spam123", "fake456", "hack789", "abc111"]

target = input("Enter Sender ID: ")

found = False

for sender in blacklist:
    if sender == target:
        found = True
        break

if found:
    print("Spam Detected..!!!!!!!!!!!")
else:
    print("Not Found.....")