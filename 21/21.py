from itertools import islice,count
def d(n):
    sum_=0
    for i in islice(count(1), int(n**0.5+1)):
        if(n%i==0):
            sum_+=i
            if (i!=n//i):sum_+=n//i
    return (sum_-n)
seen_data=set();sum_=0
for x in range(2,10001):
    if x in seen_data:continue
    image=d(x)
    if x==d(image) and x!=image:
        sum_=sum_+x+image
        seen_data=seen_data.union({x,image})
print(sum_)
        
    
