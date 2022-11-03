# Write a Python program to calculate number of days between two dates.
import calendar
import datetime
print('calculaing days between two dates')
print('')

year1 = int(input('Enter year eg(2001): '))
month1 = int(input('Enter month from 1 to 12 without leading zero: '))
day1 = int(input('Enter day from 1-31 without leading zero: '))
date1 = datetime.date(year1,month1,day1)
print(date1)

year2 = int(input('Enter year eg(2001): '))
month2 = int(input('Enter month from 1 to 12 without leading zero: '))
day2 = int(input('Enter day from 1-31 without leading zero: '))
date2 = datetime.date(year2,month2,day2)
print(date2)

days_difference = date2 - date1
print(days_difference)