s=lambda x:x+1
print(s(2))


add_sub=lambda x,y:(x+y,x-y)
a,s=add_sub(5,4)
print(a,s)

a=lambda x=2:x+1
print(a(2))


def show(a):
    print(a(8))
show(lambda x:x)

#IIFE EXPRESSION

(lambda x:print(x+1))(5)