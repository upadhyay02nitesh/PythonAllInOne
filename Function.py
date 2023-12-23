#calling function
def add(a,b):
    print(a+b)
add(2,3)

#return function
def fun(a,b):
    return a*b 
print(fun(5,4))

def fun(a,b):
    multi=a*b 
    add=a+b 
    return multi,add 
p,q=(fun(2,3))
print(p,q)

#Nested function

def outer(n):
    def inner(m):
        print("inner",m)
    print("Outer",n)
    inner(6)
outer(5)

#Passing function 1 to another function

def fun(a,b):
    return a*b 
def fun1(s):
    a=fun(5,3)
    return a+10+s
print(fun1(5))

#arguments
def add(a=4,b=2):  #formal arguments
    print(a+b)
add(5,4)  #actual arguments

def add(a,b):
    print(a,b,a+b)
add(b=2,a=1) #Keyword aguments


def sum(*args):
    s=0
    for i in args:
        s+=i 
    return s

print(sum(1,2,3,4,5))  #*args we can pass unlimited element

def show(**kwargs):
    print(kwargs)
show(A=1,B=2,C=3)
