year = int(input("Enter the year "))

if ((year%400==0) and (year%100==0)):
    print("{0} is the leap year ".format(year))

elif ((year%4==0) and year%100!=0):
    print("{0} is the leap year ".format(year))

else:
    print("{0} is not the leap year ".format(year))

