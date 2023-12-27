l=list()
print(type(l))

l1=[]
print(type(l1))

l2=[1,2.0,'a',True,2+3j]
print(l2)

print(l2[0])
print(l2[-1])

for i in l2:
    print(i,end=" ")

print()

for i in range(len(l2)):
    print(i,"=",l2[i],end=" ")

print()

n=len(l2)
i=0
while i<n:
    print(l2[i],end=" ")
    i+=1

print()  

# l3=[]
# n=int(input("Enter number of element inserteed in list "))
# for i in range(n):
#     l3.append(int(input("Enter element ")))
# print(l3)

#List Function

l4=[1,2,3,4,5]
l4.append(6)
print(l4)

l4.pop()
print(l4)

l4.pop(0)
print(l4)

l4.reverse()
print(l4)

l4.append(6)
print(l4)

l4.remove(2)
print(l4)

s=l4.index(4)
print(s)

l4.sort()
print(l4)

# l4.clear()
# print(l4)

l5=[100,200,300]
l4.extend(l5)
print(l4)


print()


#Slicing On List

a=[11,22,33,44,55]
x=a[1:3]
print(x)

x=a[-1]
print(x)

x=a[0:5:2]
print(x)

x=a[-5:-3]
print(x)

b=[1,2]
c=[5,6]
d=[7,8]

m=b+c+d 
print(m)

print(a*2)

a=[10,20,30]
b=a
b.append(25)
print(a,b)
print(id(a),id(b))

print()

c=a.copy()
print(a,c)
print(id(a),id(c))
c.append(30)
print(a,c)
print(id(a),id(c))

#Nested List
n=[[10,20,30],[40,50,60]]
for i in n:
    for j in i:
        print(j,end=" ")

print()

for i in range(len(n)):
    for j in range(len(n[i])):
        print(i,j,"=",n[i][j],end=" ")

print()

A=[1,2,3,[10,20,30]]
for i in range(len(A)):
    if type(A[i]) is list:
        for j in range(len(A[i])):
            if len(A[i])>1:
                print(i,j,"=",A[i][j])
    else:
        print(i,A[i],end=" ")

#Creating Nested List
# main_list=[]
# n=int(input("Enter the number of element "))
# m=int(input("Enter the number of element "))
# for i in range(n):
#     inner_list=[]
    
#     for j in range(m):
#         inner_list.append(int(input("Enter The Element ")))
#     main_list.append(inner_list)
# print(main_list)
        

l=[[10,20,30],[40,50,60]]
print(l[0:1])
print(l[0:1][0])
print(l[0:1][0][0])
print(l[-1][2])


