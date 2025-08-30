n = int(input("Enter Year:"))
if(n%4== 0 and n%400==0 and n%100==0):
    print("leap")
else:
    print("not leap")
