#Write a Python program to count the number of even and odd numbers from a series of numbers.
a = input("Enter a series of number")
b = len(a)
c = b + 1
even = 0
odd = 0
for i in range(1,c):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("The number of even digits are {} and number of odd digits are {}".format(even) .format(odd))


