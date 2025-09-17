date = input("enter the date:")
day,month,year = date.split("/")
day = int(day)
month=int(month)
year = int(year)
if month>0 and month<=12:
    if month == 1 or month == 3 or month == 5 or month ==7 or month == 8 or month == 10 or month == 12:
        if(day>0 and day<=31):
            print("date is valid")
        else:
            print("date is invalid")
    elif month==2:
        if (year%4==0 and year%100!=0) or year%400==0:
            if(day>0 and day<=29):
                print("valid date")
        else:
            if(day>0 and day <=28):
                print("valid date")
            else:
                print("Invalid date")
    else:
        if(day>0 and day<=30):
            print("valid date")
        else:
            print("Invalid date")
else:
    print("check range of month")
                
        
