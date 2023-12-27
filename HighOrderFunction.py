a=[10,20,30,40,50,60]

#Filter Function

def find(a):
    if a>=30:
        return True
result=filter(find,a)
for i in result:
    print(i,end=" ")

print()

#Using Lambda Function

result=list(filter(lambda n:(n>=30),a))
for i in result:
    print(i,end=" ")

print()
#Map Function

def find(a):
    return a+2
result=map(find,a)
for i in result:
    print(i,end=" ")

print()

#Using Lambda Function
result=list(map(lambda n:(n+2),a))
for i in result:
    print(i,end=" ")

print()

#Reduce Function

from functools import reduce
result=reduce(lambda n,m:(n+m),a)
print("sum of a is :",result)
