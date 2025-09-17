n=int(input("enter:"))
t=n*3

for i in range(n):
    for j in range(i+1):
        print(t,end=" ")
        t-=1
    print()
