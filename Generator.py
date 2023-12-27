def disp(a,b):
    while a<=b:
        #Yield function to retrieve generator obj to generator function
        yield a 
        a+=1
result=disp(1,5)
#Next function to retrieve element from generator obj
print(next(result))
print(next(result))
for i in result:
    print(i)

print()


#Using class and obj
    

    
