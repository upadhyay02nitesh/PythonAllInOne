n=int(input("Enter the number  -->"))
temp=n
s=len(str(n))
arm_num=0
while temp>0:
    #for remainder 
    r=temp%10
    arm_num=arm_num+r**s
    temp=temp//10

if n==arm_num:
    print(n,"is Armstrong Number")
else:
    print(n,"is not Armstrong Number")


# 153 is armstrong 
# 153=1**3+5**3+3**3=1+125+27=153


