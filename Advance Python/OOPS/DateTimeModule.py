from datetime import datetime

# get the current date and time
now = datetime.now()

print(now)

from datetime import date
# get current date
current_date = date.today()

print(current_date)
print(current_date.day)
print(current_date.month)
print(current_date.year)


from datetime import date
d = date(2022, 12, 25)
print(d)

from datetime import time
print(time())
print(time(12,12,12))
print(time(12,12,12).hour)
print(time(12,12,12).minute)
print(time(12,12,12).second)

from datetime import datetime
d=datetime(2024,12,12,12,12,12)
print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

#TimeDelta
from datetime import timedelta,date
td=timedelta(days=13 )
d=date.today()
print(d+td)

#Comparing two dates

from datetime import date 
d1=date(2024,1,18)
d2=date(2024,2,23)
print(d1==d2)
print(d1>d2)
print(d1<d2)
print(d1!=d2)

print()
#Formating of date time
# The strftime() method is defined under classes date, datetime and time. 
# The method creates a formatted string from a given date, 
# datetime or time object.
# %Y - year [0001,..., 2018, 2019,..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23
# %M - minute [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 59]

# Covert datetime type to string format

from datetime import datetime
dt=datetime.today()
print(dt,type(dt))

nt=dt.strftime("%d-%B-%Y")
print(nt,type(nt))

nt=dt.strftime("%d-%b-%y")
print(nt,type(nt))

nt=dt.strftime("%I-%M-%S")
print(nt,type(nt))


nt=dt.strftime("%H-%M-%S")
print(nt,type(nt))

# Python strptime() Method
# The strptime() method creates a datetime object from a given 
# string (representing date and time).

# Convert string format to datetime obj
print()

from datetime import datetime

dt = "25-12-2022"

date_object = datetime.strptime(dt, "%d-%m-%Y")

print("date_object =", date_object)

print()

#Sleep method

# import time
# for i in range(10):
#     if i%2==0:
#         print(i)
#         time.sleep(0.5)

#Age calculator in python

from datetime import date 
date_str = input("Enter a date (YYYY-MM-DD): ")

try:
    # Convert the input string to a datetime object
    dob = datetime.strptime(date_str, '%Y-%m-%d')
    print("Date entered:", dob)
except ValueError:
    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
# dob=date(2001,2,8)
dt=date.today()
age = (dt.year-dob.year) -((dob.month,dob.day)>(dt.month,dt.day))
print("Your age is ",age)


# n=input()
# dob=datetime.strptime(n,"%Y-%B-%d")
# print(dob)
