from itertools import islice,count
from functools import reduce
# Generalizing the problems even more
prod=[]
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
def decomposer(n):
    global prod
    num=n
    for i in primes_list:
        if i>num:
            break
        if num%i!=0:
            continue
        else:
            count=0
            while not(n%i):
                n/=i
                count+=1
            n=num
            if count>prod.count(i):
                prod.extend([i]*(count-prod.count(i)))
                
start=1
end=20
primes_list=[x for x in range(2,end+1) if is_prime(x)]#preloading the factor primes
for num in range(start,end+1):
    if num==1:
        prod.append(1)
    elif num in primes_list:
        prod.append(num)
    else:
        decomposer(num)
product = reduce((lambda x, y: x * y), prod)
print(product)
        
