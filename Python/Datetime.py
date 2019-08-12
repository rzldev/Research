
## The datetime module supplies classes for manipulating dates and times in both simple and complex ways
## Import datetime module
import datetime

## Create a date
date = datetime.date(2019, 8, 11)
print(date)

## Print today date
today = datetime.date.today()
print(today)
# print datetime with some format
print(today.day)
print(today.weekday())
print(today.isoweekday())
# weekday between 0 - 6
# weekday between 1 - 7

## A duration expressing the difference between two date using timedelta
tmdelta =  datetime.timedelta(days=7)
print(tmdelta)
print(today + tmdelta)
print(today - tmdelta)

## Check my age
import math
bday_date = datetime.date(1999, 1, 1)
age = today - bday_date
print(math.trunc(age.days / 365))

## Create a time
time = datetime.time(9, 34, 00)
print(time)

## Create a datetime
dttime = datetime.datetime.today()
print(dttime)
# Print with some specific format
print(dttime.day)
print(dttime.year)
print(dttime.minute)
print(dttime.microsecond)

## print datetime.today, datetime.now, datetime.utcnow
# UTC(Coordinated Universal Time)
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
# today() return the current local date
# now() return the current local date and time
# utcnow() return the current UTC date and time, with tzinfo None

## pytz brings the Olson tz database into Python, this library allows accurate and cross platform timezone
import pytz
## Print datetime with pytz format
print(datetime.datetime(2019, 8, 12, 10, 16, 45, tzinfo=pytz.UTC))

## Convert utcnow into pytz package
utctime = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(utctime)

## Print datetime from specific timezone
utctimenow = datetime.datetime.now(tz=pytz.UTC)
ustime = utctimenow.astimezone(pytz.timezone('US/Mountain'))
print('US Time :', ustime)
tokyotime = ustime.astimezone(pytz.timezone('Asia/Tokyo'))
print('Tokyo Time :', tokyotime)

## Print all the timezones
# for tz in pytz.all_timezones :
#     print(tz)

## Convert datetime into string
usdate = ustime.strftime('%B %d, %Y')
print(usdate)

## Convert string into datetime
usdatestr = 'August 11, 2019'
new_usdate = datetime.datetime.strptime(usdatestr, '%B %d, %Y')
print(new_usdate)
