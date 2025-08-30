n = int(input("enter the number:"))
flag = True
i =2;
while(i<=(n/2)):
    if(n%i==0):
        flag=False
        break
    i+=1


if(flag):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
