from functools import lru_cache
@lru_cache(3)
def fib(n):
    if n==1:return 1
    if n==0:return 0
    return fib(n-1)+fib(n-2)
n=1
while len(str(fib(n)))!=1000:n+=1
print(n)
