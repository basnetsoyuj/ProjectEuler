from itertools import islice,count
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
i=1
n=2
while(i<=10001):
    if is_prime(n):
        if i==10001:
            print(n)
        i+=1
    n+=1
