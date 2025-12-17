
import copy

original = [[1, 2], [3, 4]]
shallow_copy = original[:]            # or list(original)
deep_copy = copy.deepcopy(original)

original[0].append(99)

print("Original:", original)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
