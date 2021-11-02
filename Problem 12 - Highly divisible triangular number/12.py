from itertools import islice,count
triangle_num=lambda n:int(n*(n+1)*0.5)
divisors=0;n=1;max_=0
while(divisors<=500):
    num=triangle_num(n)
    factors=set()
    for i in islice(count(1), int(num**0.5+1)):
        if(num%i==0):
            factors.update({i,num//i})
    divisors=len(factors)
    if divisors>max_:
        max_=divisors
    n+=1
print(int(n*(n-1)*0.5))
