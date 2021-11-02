total=0;the_numbers=[]
for x in range(2,1000001):
    sum_=sum([(int(i))**5 for i in str(x)])
    if sum_==x:
        total+=x
print(total)
