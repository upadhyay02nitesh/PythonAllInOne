# 1.
n=int(input("Enter the number  -->"))


import math
print(math.factorial(n))

# 2.

fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# 3.

#Using recursion
def fact(n):
    if n==0 or n==1:
        return 1 
    else:
        return n*fact(n-1)
print(fact(n))
