from itertools import islice,count
def is_prime(n):
    for i in islice(count(2),int(n**0.5-1)):
        if n%i==0:
            return 0
    return 1
def lex_permutations(l):
    if len(l)==1:return l
    permutations=list()
    for x in l:
        for sub_permutations in lex_permutations([n for n in l if n!=x]):
            permutations.append(x+sub_permutations)
    return permutations

for x in range(9,0,-1):
    list_=[str(i) for i in range(1,x+1)]
    permutations=[int(j) for j in lex_permutations(list_) if is_prime(int(j))]
    if permutations:
        print(max(permutations))
        break