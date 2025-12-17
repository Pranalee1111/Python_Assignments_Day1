
nested = [[1, 2, 3], [4, 5], [10], [7, 8, 9, 10]]
sums = []
for inner in nested:
    total = 0
    for x in inner:
        total += x
    sums.append(total)
print("Nested list:", nested)
