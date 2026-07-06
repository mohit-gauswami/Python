prices = [10000, 15000, 22000, 35000, 50000, 65000, 80000]

target = 50000

low = 0
high = len(prices) - 1
index = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        index = mid
        high = mid - 1
    else:
        low = mid + 1

if index != -1:
    print("First Product Price >= 50000 is", prices[index])
    print("Index:", index)
else:
    print("No Product Found")