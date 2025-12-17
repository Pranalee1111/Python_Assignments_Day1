

t = ([1, 2, 3], {"x": 10, "y": 20}, ["a", "b"])
print("Before:", t)

t[0].append(99)
t[1]["z"] = 30
t[2][0] = "A"

print("After:", t)
