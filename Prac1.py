#Write a program to count the number of vowels, consonants, digits, and
# special characters in a given string.

s = "Hello123@4$"
print(s)
l1 = {'a','e','i','o','u'}
vowels=0
conson =0
digits=0
characters=0


for i in s:
    if i.isalpha():
        if i.lower() in l1:
            vowels+=1
        else:
            conson+=1
    elif i.isdigit():
        digits+=1
    else:
        characters+=1

print(vowels)
print(conson)
print(digits)
print(characters)






