from itertools import islice,count
triangle_number=lambda n:int(n*0.5*(n+1))
max_no_divisor=500
num=1;n=1;max_=0
divisors=0
while(divisors<=500):
    divisors=0
    for i in islice(count(1),num):
        if num%i==0:   
            divisors+=1
        if divisors+num-i<max_no_divisor:
            break
        if divisors>max_:
            print(num,divisors,i)
            max_=divisors
    num=triangle_number(n+1);n+=1
print(num,divisors)
