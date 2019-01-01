from math import factorial as f
count=0
for n in range(1,101):
    for r in range(0,n+1):
        nCr=f(n)/(f(r)*f(n-r))
        if nCr>1000000:count+=1
print(count)
