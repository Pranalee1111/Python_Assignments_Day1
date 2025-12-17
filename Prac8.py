

nums = [12, 35, 1, 10, 34, 1]
if len(nums) < 2:
    print("List must have at least two elements.")
else:
    largest = max(nums)
    filtered = []
    for x in nums:
        if x != largest:
            filtered.append(x)
    if not filtered:
        print("All elements are equal. No second largest.")
    else:
        second_largest = max(filtered)
        print("List:", nums)
        print("Second largest:", second_largest)
