n=int(input("Enter the number -->"))
#Using for loop
for i in range(1,n+1):
    print(i,end=" ")

print()
#Sum of natural number
s=0
for i in range(1,n+1):
    s+=i 
print(s)

print()
#Using Factorial sum of natural number
def fun(n):
    if n==1:
        return 1 
    else:
        return n+fun(n-1)
print(fun(n))