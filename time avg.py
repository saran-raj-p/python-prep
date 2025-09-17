def average(l,start):
    step=3
    s=start
    hs=0
    ms=1
    ts=2
    #print(s+hs)
    hour1=l[s+hs]
    hs+=step
    hour2=l[s+hs]
    min1=l[s+ms]
    ms+=step
    min2=l[s+ms]
    t1=l[s+ts]
    ts+=step
    t2=l[s+ts]
    #print(type(hour1))
    #print(type(min1))
    if(t1=="PM" and hour1!=12):
        hour1+=12
    if(t2=="PM" and hour2!=12):
        hour2+=12
    avg=(hour2+min2/60)-(hour1+min1/60)
    if(avg<0):
        avg*=-1
    return avg
    
        
        
    
    




time =["10:00 AM to 11:00 AM","11:00 AM to 12:30 PM","12:30 PM to 1:15 PM","1:15 PM to 2:00 PM","2:00 PM to 3:45 PM"]
l =[]
start=0
total=0
step=6
for i in range(len(time)):
    t=""
    for j in time[i]:
        if(j==":"):
            #print(t)
            l.append(int(t))
            t=""
        elif(j=='t' or j=='o'):
            continue
        elif(j=='A' or j=='P'):
            #print(t)
            l.append(int(t))
            t=""
            t+=j
        elif(j=='M'):
            t+=j
            l.append(t)
            t=""
        else:
            t+=j
    total+=average(l,start)
    start+=step

    

print(total/(len(time)))
        
