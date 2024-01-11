n=int(input("Enter the Year -->"))
if (n%4==0 and n%100!=0) or n%400==0:
    print(n,"is Leap year")
else:
    print(n,"is not Leap Year")