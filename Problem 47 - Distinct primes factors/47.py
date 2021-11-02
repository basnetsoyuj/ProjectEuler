from itertools import islice,count
n=2
def is_prime(n):
    for num in islice(count(2),int(n**0.5-1)):
        if n%num==0:
            return 0
    return 1
prime_list=[x for x in range(2,700) if is_prime(x)]
while 1:
    a,b,c,d=0,0,0,0
    for i in prime_list:
        if i>n+3 and i>n+2 and i>n+1 and i>n:break
        if n%i==0:a+=1
        if (n+1)%i==0:b+=1
        if (n+2)%i==0:c+=1
        if (n+3)%i==0:d+=1
    if a==b==c==d==4:
        print(n)
        break
    n+=1
        
