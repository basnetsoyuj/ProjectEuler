from itertools import islice,count
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
def sum_returner(n):
    sum_=0
    for i in islice(count(2),n-2):
        if is_prime(i):
            sum_+=i
    return sum_
print(sum_returner(2000000))
