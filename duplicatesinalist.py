lst = [1, 2, 3, 2, 4, 5, 1, 6,5,1,1,1]

seen = set()
duplicates = set()

for item in lst:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(list(duplicates))