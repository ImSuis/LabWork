#Given the integer N - the number of minutes that is passed since midnight - how many
#hours and minutes are displayed on the 24h digital clock?
N = int(input("Enter the number of time passed since midnight in minutes"))
hour = (N // 60)
min = (N % 60)
print ("The hour is : {}" .format(hour))
print("The muniute is : {}" .format(min))
