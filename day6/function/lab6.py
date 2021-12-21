#.No.6 Write a Python program to reverse a string. 
def reverse(word):
    i = len(word)
    k = i+1
    w = ""
    for j in range(1,k):
        l = i-j
        w = w + word[l]
    print(w)
word=input("enter a word: ")
reverse(word)