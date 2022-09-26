workday = [1,2,3,4,5]
weekend = [6,7]
day = int(input("enter a day of week "))
if day in workday:
    print("workday")
elif day in weekend:
    print("weekend")
else:
    print("It's not a day of week")