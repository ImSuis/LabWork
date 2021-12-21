#No.1 Write a Python function to find the Max of three numbers 
def num(firstNum,secondNum,thirdNum):
    if firstNum>secondNum and firstNum > thirdNum:
        print("the max number is :",firstNum)
    elif secondNum > firstNum and secondNum > thirdNum:
        print("the max num is :",secondNum)
    else:
        print("the max num is :",thirdNum)

num(1,4,3)
