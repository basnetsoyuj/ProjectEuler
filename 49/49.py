from itertools import islice,count
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
def permutations(l):
    if len(l)==1:return l
    p=list()
    for x in range(0,len(l)):
        for sub_permutations in permutations([l[n] for n in range(0,len(l)) if n!=x]):
            p.append(l[x]+sub_permutations)
    return p
for x in range(1000,10000):
    if not is_prime(x):continue
    list_=[int(y) for y in permutations(list(str(x))) if int(y)>x and is_prime(int(y))]
    for y in list_:
        list_1=[i for i in list_ if (i>y and i-y==3330 and y-x==3330)]
        if list_1:
            print(f"{x}{y}{list_1.pop()}")
            break
