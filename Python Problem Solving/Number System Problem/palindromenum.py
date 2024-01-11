n=int(input("Enter the number  -->"))

temp=n
reverse_num=0
while temp>0:
    #for remainder 
    r=temp%10
    reverse_num=reverse_num*10+r 
    temp=temp//10

if n==reverse_num:
    print(n ,"is Palindrome number")
else:
    print("not a Palindrome number")
