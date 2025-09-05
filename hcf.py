n1 = 144
n2 = 24

small = 0;
great=0

if n1<n2:
    small = n1
else:
    small = n2

if n1>n2:
    great = n1
else:
    great = n2

x = great%small
if(x==0):
    print(small)
else:
    t = small
    while(t>0):
        t = t%x

    if(t==0):
        print(x)   

