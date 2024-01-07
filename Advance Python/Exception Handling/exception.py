# Exception-- run time error handled by programmer

# types -
# 1. Built in - already avaialble in python
# 2. User defined - where user can also define own exception

#Exception HAndling - 

# a=10
# b=0
# c=a/b 
# print(c)   #raise exception ZeroDivisionError

# Handling the exception
a=10
b=0
try:
    c=a/b 
    print(c)

except ZeroDivisionError:
    print("ZeroDivision Error occured")

else:
    for i in range(2):
        print("Else part if exception not occur")
finally:
    print("Completed")


# Try - which block raised exception

# Except - Handle the Exception

#Else -- when no exception occur then this block will be executed

#Finally - Always executed 
    
print("when you don't know which exception occur")
a=10
b=0
try:
    c=a/d
    c=a/b
    print(c)

except Exception as e:
    print(e,"Exception Error occured")

else:
    for i in range(2):
        print("Else part if exception not occur")
finally:
    print("Completed")
    
print("User defined ")
print()
# How To create User defined Exception
# 1.creating exception class Using Exception base class
# 2. Raising Exception
# 3. Handling Exception

class BalanceException(Exception):
    pass 

def check_balance():
    money=10000
    withdraw=9000
    balance=money-withdraw

    if (balance<=2000):
        raise BalanceException("insufficient Balance please withdraw above 2000")
    print(balance)

try:
    check_balance()

except BalanceException as e:
    print(e)