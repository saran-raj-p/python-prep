def armstrong(n):
    sum =0
    t = n
    power = len(str(n))
    while(t>0):
        x = t%10
        sum += x**power
        t = t//10

    if(sum==n):
        return n
    else:
        return 0




low = int(input("enter the start:"))
high = int(input("enter the start:"))

for i in range(low,high+1):
    c = armstrong(i)
    if c==0:
        continue
    else:
        print(c)
