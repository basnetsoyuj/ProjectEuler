from math import factorial
sum_=0
for x in range(10,50000):
    f=[factorial(int(i)) for i in list(str(x))]
    if x==sum(f):
        sum_+=x
print(sum_)
