m=int(input("Enter the number of range  -->"))
for n in range(10,m+1):
    temp=n
    s=len(str(n))
    arm_num=0
    while temp>0:
        #for remainder 
        r=temp%10
        arm_num=arm_num+r**s
        temp=temp//10

    if n==arm_num:
        print(n,end=" ")
