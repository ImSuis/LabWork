#Write a Python program to count the number of even and odd numbers from a series of numbers.
num = [1,2,3,4,5,6,7]
odd,even = 0,0
for i in range(len(num)):
    w = num[i]
    if w%2 == 0:
        odd = odd + 1
    else:
        even = even + 1
print(f"The Total Number of Even are {even} and odd are {odd} ")


