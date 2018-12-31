from itertools import islice,count
def is_prime(n):
    if n==1:return 0
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
def trunc_prime(x):
    if not is_prime(x):return 0
    intdiv=10
    for _ in range(1,len(str(x))):
        if (not is_prime(x//intdiv))or (not is_prime(x%intdiv)):
            return 0
        intdiv*=10
    return 1
n=1
num=11
sum_=0
while n<=11:
    if trunc_prime(num):
        sum_+=num
        n+=1
    num+=1
print(sum_)
