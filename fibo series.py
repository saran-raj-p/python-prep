n = int(input("enter the number:"))

a=0
b=1
for i in range(n):
    print(f"{a},",end=" ")
    a,b = b,a+b
    
    
