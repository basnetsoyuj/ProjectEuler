n=1
sum_=0
while(n<=1000):
    sum_+=n**n
    n+=1
print(sum_%(10**10))
