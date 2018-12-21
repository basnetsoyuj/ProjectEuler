sum_=0
n=3
#n=5
for num in range(1,1000):
    if num%3==0 or num%5==0:
        sum_+=num
print(sum_)
