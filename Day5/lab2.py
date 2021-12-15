#write a program to convert temperature to and from celcius, fahrenhite
degree = (input("Enter C for celsius and F for fahrenhite"))
temp = float(input("Enter the temparature"))
if degree == "C":
    conv = ((temp * 9)/5) +32
    print(conv ,"F")
else:
    conv = (5/9) * (temp -32)
    print(conv,"C")
