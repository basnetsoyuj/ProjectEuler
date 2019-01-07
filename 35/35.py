seen=set()
from itertools import islice,count
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
            if n%i==0:
                return 0
    return 1
def is_prime_list(list_):
    for n in list_:
        if not is_prime(n):return 0
    return 1
for x in islice(count(2),1000000):
    if not is_prime(x):continue
    if x in seen:continue
    strx=str(x)
    list_=l=[int(strx[n:]+strx[:n]) for n in range(0,len(strx))]
    if is_prime_list(list_):
        seen.update(list_)
print(len(seen))
