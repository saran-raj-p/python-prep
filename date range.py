def nextday(day,month,year):
    maxday=0
    if month==1 or month==3 or month== 5 or month== 7 or month==8 or month==10 or month==12:
        maxday=31
        day+=1
        if(day<=maxday):
            return day,month,year
        elif(day>maxday and month==12):
            day=1
            month=1
            year+=1
            return day,month,year
        else:
            if(day>maxday):
                day=1
                month+=1
                return day,month,year
            
    elif month==2:
        if(year%4==0 and year%100!=0 or year%400==0):
            maxday=29
            day+=1
            if(day<=maxday):
                return day,month,year
            elif(day>maxday):
                day=1
                month+=1
                return day,month,year
        else:
            maxday=28
            day+=1
            if(day<=maxday):
                return day,month,year
            elif(day>maxday):
                day=1
                month+=1
                return day,month,year
    elif month== 4 or month ==6 or month==9 or month==11:
        maxday=30
        day+=1
        if(day<=maxday):
            return day,month,year
        else:
            day=1
            month+=1
            return day,month,year
            
        





start=input("enter date:")
end=input("enter date:")
startday=0
startmonth=0
startyear=0
endday=0
endmonth=0
endyear=0
t=""
for i in start:
    if(i=='/' and startday==0):
        startday=int(t)
        t=""
    elif(i=='/' and startmonth==0):
        startmonth = int(t)
        t=""
    else:
        t+=i
startyear=int(t)
t=""
for i in end:
    if(i=='/' and endday==0):
        endday=int(t)
        t=""
    elif(i=='/' and endmonth==0):
        endmonth = int(t)
        t=""
    else:
        t+=i
endyear=int(t)
l=["12/08/2025","10/04/2025","04/06/2025"]
day,month,year=startday,startmonth,startyear
find=False
while True:
    day,month,year=nextday(day,month,year)
    if(day>endday and month==endmonth and year==endyear):
        print("dates not found in range")
        break;
    now=""+str(day)+"/"+"0"+str(month)+"/"+str(year)
    print("now:",now)
    for i in l:
        if i==now:
            print(i)
            find=True
            break
    if(find):
        break;
       

