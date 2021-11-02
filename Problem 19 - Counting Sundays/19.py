days={1:31,2:0,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
leap_years={x for x in range(1901,2000)if x%4==0 and (x//4)%2==0}.union({2000})
counter=0
dayint=2
for year in range(1900,2001):
    if year in leap_years:
        days[2]=29
    else:
        days[2]=28
    for month in range(1,13):
        for day in range(1,days[month]+1):
            if day==1 and dayint==1 and year!=1990:
                counter+=1
            if dayint==7:
                dayint=1
            else:
                dayint+=1
print(counter)
        
