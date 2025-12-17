
text = input("Enter a string: ")
seen = ""
if text == "":
    print("The string is empty. Nothing to count.")
else:
    print("\nCharacter frequencies:")
    for ch in text:
        if ch not in seen:
            print(f"'{ch}' appears {text.count(ch)} time(s)")
            seen += ch
