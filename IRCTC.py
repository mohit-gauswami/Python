l1 = [2, 5, 8, 12]
l2 = [1, 3, 7, 10, 15]

merged = []

i = 0
j = 0

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merged.append(l1[i])
        i += 1
    else:
        merged.append(l2[j])
        j += 1

while i < len(l1):
    merged.append(l1[i])
    i += 1

while j < len(l2):
    merged.append(l2[j])
    j += 1

print("Merged List:", merged)