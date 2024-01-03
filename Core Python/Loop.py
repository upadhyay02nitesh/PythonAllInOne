# For Loop
s="CodeshopByNitesh"
for i in s:
    print(i,end=" ")
print("Program executed")



for i in range(5):
    print(i)



for i in range(len(s)):
    print(i,s[i],end=' ')
print()


for i in range(3):
    print("outer",i,)
    for i in range(4,10):
        print(" ","inner",i)


for i in range(10,-1,-1):
    print(i,end=" ")
else:
    print("Done")

# While Loop

i=0
a=10
while a>0:
    print(a,end=" ")
    a-=1

i=0
while True:
    i+=1
    print(i,end=" ")
    if i==3:
        break

i=0
a=10
while i<a:
    print("Outer",i)
    i+=1
    j=0
    while j<a:
        print(" ","inner",j)
        j+=1
        