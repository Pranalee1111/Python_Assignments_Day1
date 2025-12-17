
t = (5, 1, 9, 3, 7, 2)

if len(t) == 0:
    print("Empty tuple.")
else:
    maximum = t[0]
    minimum = t[0]
    for x in t[1:]:
        if x > maximum:
            maximum
            maximum = x
        if x < minimum:
            minimum = x
    print("Tuple:", t)
    print("Max:", maximum)

