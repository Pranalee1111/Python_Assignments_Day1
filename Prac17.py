
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

common = A & B
A_without_common = A - common
B_without_common = B - common

print("A without common:", A_without_common)
print("B without common:", B_without_common)
