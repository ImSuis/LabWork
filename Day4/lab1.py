#check whether the given year is leap year or not
year=int(input("Enter a year"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Common year")