n=int(input("Enter the number  -->"))

sm=0
while n>0:
    #for remainder 
    r=n%10
    sm=sm+r 
    n=n//10
print(sm)


# if n=123
#  then r=123%10=3
#       sm=0+3
#     n=123//10=12
 

#  in last 3+2+1=6

 
