sum_=1;n=1
side=2
while n<=(1000)**2:
    for _ in range(1,5):
        n+=(side-1)*2
        sum_+=n
    side+=1
print(sum_)
