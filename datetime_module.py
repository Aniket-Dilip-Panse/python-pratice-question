import datetime

# to create our own date use dattime.date(year,month,day) function
# <=============== NOTE :- do not use float value inside it and never use 02 or 03 for any month or day
created_date = datetime.date(2001,12,21)
print(created_date)

# to print todays local date use datetime.date.today()
today_date = datetime.date.today()
print(today_date)

# if we want only year or month or day use .year , .month , .day for created variable it will return in integer
print(f"current working Year = {today_date.year}")
print(f"current working Month = {today_date.month}")
print(f"current working Date = {today_date.day}")

# if we want to print weekday use .weekday() or isoweekday() it will return integer value
# .weekday monday = 0 and sunday = 6
# .isoweekday monday = 1 and sunday = 7

# print(f"current working day = {today_date.weekday()}")
# print(f"current working day = {today_date.isoweekday()}")

today_day = today_date.weekday()
today_isoday = today_date.isoweekday()
def TodayDay():
    if today_day == 0:
        print(f"current working day = Monday")
    elif today_day == 1:
        print(f"current working day = Tuesday")
    elif today_day == 2:
        print(f"current working day = Wednesday")
    elif today_day == 3:
        print(f"current working day = Thursday")
    elif today_day == 4:
        print(f"current working day = Friday")
    elif today_day == 5:
        print(f"current working day = Saturday")
    elif today_day == 6:
        print(f"current working day = Sunday")
    else:
        print('invalid day holiday')
TodayDay()