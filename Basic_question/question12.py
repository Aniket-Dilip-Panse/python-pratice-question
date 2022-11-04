# Write a Python program to print the calendar of a given month and year.
import calendar
year = int(input('Enter the year for which you want the calender '))
month = int(input('Enter the month for which you want the calender '))
print(calendar.month(year,month))

# to print whole calender of any year use below code calender.calender(year)
print(calendar.calendar(2001))

# To check whether the year is leap year or not use calender.isleap(year)
print(calendar.isleap(2001))