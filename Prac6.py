
nums = [1, 2, 2, 3, 1, 4, 3, 5, 5]
unique_list = []
for x in nums:
    if x not in unique_list:
        unique_list.append(x)
print("Original:", nums)
print("Without duplicates:", unique_list)
