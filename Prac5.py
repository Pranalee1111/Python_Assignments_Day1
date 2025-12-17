
s = input("Enter a string: ")

print("Original string:", s)

try:
    s[0] = 'X'  # Attempt to modify the first character
except TypeError as e:
    print("Error occurred:", e)

if s != "":
    new_s = 'X' + s[1:]  # Correct way: create a new string
else:
    new_s = s

