#Write a Python program that accepts a string and calculate the number of digits and letters
word = input("Enter string")
letterCount,numberCount = 0,0
for i in word:
    if i.isalpha():
        letterCount = letterCount + 1
    if i.isnumeric():
        numberCount = numberCount + 1
print(f"The toal letter is: {letterCount} and number is: {numberCount}.")