import calendar
year=int(input("enter the year:"))
leap_year=calendar.isleap(year)
if leap_year:
    print("the given year is leap year")
else:
    print("the given year id non-leap year")
