start=0
s="the boy is big "
l=[]
for i in range(len(s)):
    if(s[i]==" "):
        l.append(s[start:i])
        start = i+1
    elif(i==len(s)-1):
        l.append(s[start:i+1])

print(l)

t=""
for i in range(len(l)-1,-1,-1):
    if i==0:
        t+=l[i]
    else:
        t+=(l[i]+" ")

print(t)
        
    
