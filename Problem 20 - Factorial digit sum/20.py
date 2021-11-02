sum_=0;factorial=1
for x in range(1,101):
    factorial*=x
factorial=str(factorial)
for x in factorial:
    sum_+=int(x)
print(sum_)
