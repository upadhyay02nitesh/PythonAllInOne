m=int(input("Enter the number of range -->"))
for n in range(1,m+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
            
        else:
            print(n,end=" ")