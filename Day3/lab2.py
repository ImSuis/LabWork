#WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
a = int(input("Enter your English marks:"))
b = int(input("Enter your Maths marks:"))
c = int(input("Enter your Science marks:"))
d = int(input("Enter your Social marks:"))
total = a+b+c+d
percentage = total/4
if (percentage > 70):
    print(f"Distinction")
elif (percentage > 60 and percentage <=70):
    print(f"First div")
elif (percentage > 40 and percentage <=60):
    print(f"pass")
else:
    print(f"fail")
print("The total marks is {}".format(total))
print("The total percentage is {} %".format(percentage))

