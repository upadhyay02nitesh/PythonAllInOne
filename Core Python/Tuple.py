t=(2,)
print(type(t))

t=(1,2.0,'a',2+3j)
for i in t:
    print(i,end=" ")

print()

for i in range(len(t)):
    print(i,"=",t[i],end=" ")

print()

n=len(t)
i=0
while i<n:
    print(t[i],end=" ")
    i+=1

print()

#Slicing

t=(1,2,3,4,5)
print(t[2:3])
print(t[-4:-3])
print(t[-4:])

b=(6,7,8,9)
print(t+b)

#Deleting Tuple

t=(1,2,3,4,5)
#DElete entire tuple its structure also not exist
del(t)
# print(t)


#Input from user
# t=[]
# n=int(input("How amny element "))
# for i in range(n):
#     t.append(int(input("Enter the element ")))
# print(tuple(t))

#Tuple has not much function because its immutable
t=(11,22,(1,2,3))
for i in range(len(t)):
    if type(t[i]) is tuple:
        if len(t[i])>1:
            for j in range(len(t[i])):
                print(i,j,"=",t[i])
    else:
        print(i,"=",t[i])

#Slicing on nested tuple
        
a=((1,2,3),(4,5,6))

print(a[0][0])
print(a[-1][1])

#List Of tuple

a=[(10,20),(30,40)]
for i in a:
    print(type(i))

#Tuple of List

a=([10,20],[30,40])
for i in a:
    print(type(i))