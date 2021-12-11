#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.
firstNum = int(input("Enter first number"))
secondNum = int(input("Enter second number"))
thirdNum = int(input("Enter third number"))
sumA=firstNum + secondNum + thirdNum
if(firstNum == secondNum or firstNum==thirdNum or secondNum==thirdNum):
    print("The sum is 0")
else:
    print("The sum is : {}".format(sumA))
