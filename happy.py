def happy(n):
    if n==1:
        return 1
    l=[]
    if(n in l):
        return 0
    x=n
    sum=0
    while(x>0):
        temp = x%10
        sum+=temp*temp
        x//=10
    l.append(sum)

    happy(sum)



n = int(input("enter the digits:"))
if(happy(n)==0):
    print("unhappy")
else:
    print("happy")
