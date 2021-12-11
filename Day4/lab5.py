totalClass = int(input("Enter the total number of class held: "))
attended = int(input("Enter the total number of class attended: "))
percentage = (attended/totalClass)*100
if (percentage >= 75):
    print("they are  allowed to sit in exam")
else:
    print("they are not allowed to sit in exam")