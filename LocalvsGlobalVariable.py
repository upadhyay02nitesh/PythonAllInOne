#Local Variable
def add(a):
    x=10 #Local Variable
    print(x)
    print(a)
add(5)
# print(x) #Not Accessible from outside

#Global Variable
g=100
def fun(a):
    b=10
    print(a+g+b)
    print(g,"in")
fun(10)
print(g,"Out")


#Function Priority for local varialbe if same name are there

a=10
def fun():
    a=10
    print(a)
fun()


#if you want to proroty of global in use inside the function
a=10
def fun():
    global a 
    a=a+10
    print(a)
fun()