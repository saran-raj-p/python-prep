date = input("date")
s = ""

for i in date:
    if(i=='/'):
        continue
    else:
        s+=i

t=""

r=len(s)-1
while(r>=0):
    t+=s[r];
    r-=1
    

if(s==t):
    print(True)
else:
    print(False)
