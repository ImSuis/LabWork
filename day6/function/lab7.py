#No.7 Write a Python function that accepts a string and calculate the number of upper case letters 
#and lower case letters.
def checkCase(word):
    i = str(word)
    upperCount = 0
    lowerCount = 0
    if i.isupper:
        upperCount += 1
    else:
        lowerCount += 1
    print(f"Lower count is {lowerCount} and upper count is {upperCount}")
word = input("Enter a word: ")
checkCase(word)

