# if n==6
# then fibo series is 0,1,1,2,3,5

print("fibonacci series")

n=int(input("Enter the number  -->"))
a,b=1,0
for i in range(n):
    temp=a
    a=b
    print(a,end=" ")
    b=temp+b

print()
print("fibonacci number -->")
# example if n==6 then fibo num=5
    
a,b=1,0
for i in range(n+1):
    temp=a
    a=b
    b=temp+b
print(a)

#using Recursion Generate series 

print("fibonacci number -->")
def fibo(n):
    if n<=1:
        return n
   
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(n))



print("fibonacci series")

def fibo(n):
    if n<=1:
        return n

    else:
        return fibo(n-1)+fibo(n-2)
for i in range(n):
    print(fibo(i),end=" ")
