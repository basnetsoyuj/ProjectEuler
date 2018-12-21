from itertools import islice,count
def is_prime(n):
#to check prime we can go from (2,int(sqrt(n)))
# let (a,b)be the factors of n
#if it contains factor > int(sqrt(n)),say a
#other factor b should be < int(sqrt(n)) as if it is greater a*b where both are greater than sqrt(n) then a*b>n(contradiction)
#int(n-1) to return 2 and 3 as prime
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1

number=600851475143
for x in islice(count(int(number**0.5),-1),int(number**0.5)):
    if number%x==0 and is_prime(x):
        print(x)
        break
