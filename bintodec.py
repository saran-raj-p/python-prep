n = int(input("enter the digit:"))
t = n
sum=0
power=0
while(t>0):
    rem = t%10
    sum += ((2**power)*rem)
    power +=1
    t //=10

print(sum)
