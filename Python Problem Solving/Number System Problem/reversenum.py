n=int(input("Enter the number  -->"))

reverse_num=0
while n>0:
    #for remainder 
    r=n%10
    reverse_num=reverse_num*10+r 
    n=n//10
print(reverse_num)

