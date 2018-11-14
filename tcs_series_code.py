n=int(input("enter any number:"))
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=" ")
    else:
        for e in range(i,i+1):
            power=e//2
            print(2**power,end=" ")