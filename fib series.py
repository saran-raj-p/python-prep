n = int(input("enter:"))
first=0
second=1
for i in range(n):
    print(first)
    first,second=second,first+second
    
