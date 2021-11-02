max_=0
for a in range(1,100):
    for b in range(1,100):
        sum_=0
        n=a**b
        while n!=0:
            sum_+=n%10
            n=n//10
        if sum_>max_:
            max_=sum_
            h=a,b
print(max_)
        
