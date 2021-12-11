age = int(input("enter the age:"))
gender = str(input("enter the gender"))
if (gender == "F"):
    print("she will work in urban area")
elif (gender == "M" and age >=20 and age <=40):
    print("He may work anywhere")
elif (gender == "M" and age > 40 and age <=60 ):
    print("he will work in urban areas")
else:
    print("ERROR")