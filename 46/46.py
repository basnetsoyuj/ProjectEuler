from itertools import islice,count
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
n=4
while(1):
    if not is_prime(n) and n%2==1:
        counter=0
        for y in range(2,n):
            if is_prime(y) and (n-y)%2==0 and (((n-y)//2)**0.5==int(((n-y)//2)**0.5)):
                break
        else:
            print(n)
            break
    n+=1
