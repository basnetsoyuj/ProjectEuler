def is_abundant(x):
    sum_=0
    for y in range(1,int(x**0.5+1)):
        if x%y==0:
            sum_+=y
            if(y!=x/y and y!=1):sum_+=x/y
        if sum_>x:return 1
    if sum_<=x:return 0
list_=[x for x in range(12,28213) if is_abundant(x)]
check=set(list_)
sum_=0
def is_sum(x):
    for y in list_:
        if (y>x):
            return 0
        if (x-y) in check:return 1
    return 0
for x in range(1,28214):
    if not is_sum(x):sum_+=x
print(sum_)
