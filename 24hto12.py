s1 = input("enter the date:")
time = s1.split(":")
hr = int(time[0])
min = int(time[1])
if(hr>12):
    print(f"{hr-12}:{min}")
else:
    print(f"{hr}:{min}")
