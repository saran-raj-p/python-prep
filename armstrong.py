n = int(input("enter the number:"))
sum = 0
x = n
while(x>0):
    rem = x%10;
    sum += (rem**3)
    x = x//10

if(sum==n):
    print(f"{n} is armstrong")
else:
    print(f"{n} is not armstrong")
