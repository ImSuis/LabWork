#find BMI of a person where take mass and height as input from the user
mass = int(input("Enter mass in kg"))
height = int(input("Enter height in meter"))
bmi = mass/(height)**2
print("The BMI of a person is {} kg/m\u00b2" .format(bmi))
