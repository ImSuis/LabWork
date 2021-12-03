#convert seconds to day, hours, minutes
sec = int(input("enter second"))
day = sec/(60*60*24)
hrs = sec/(60*60)
min = sec/(60)
print("The second in day is {}." .format(day))
print("The second in hour is {}." .format(hrs))
print("The second in minute is {}." .format(min))
