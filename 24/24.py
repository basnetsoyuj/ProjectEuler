#even though this question can be brute forced ,there is a better solution
# we know , we have 10 digits ie [0,9]
# so its same as saying x + permutation([0-9 except x])
# so 0 _ _ _ _ _ _ _ _ _ has 362880 possibilities
# also 1 _ _ _ _ _ _ _ _ _  has 362880 possibilities
# so total possibilities exhausted =725760
# but with 2_ _ _ _ _ _ _ _ _ it becomes 1088640 which is > 1000000 the Lexicographic
# permutation we want so it is in 2 _ _ _ _ _ _ _ _ _  which reduces problem from 10! to 9!
# it can further be reduced ,but im bored lol
iter_=0
def lex_permutations(l):
    global iter_
    if len(l)==1:return l
    permutations=list()
    if iter_==0:
        iter_+=1
        for sub_permutations in lex_permutations(l):
            permutations.append('2'+sub_permutations)
    else:
        for x in l:
            for sub_permutations in lex_permutations([n for n in l if n!=x]):
                permutations.append(x+sub_permutations)
    return permutations
permut=lex_permutations([str(i)for i in range(0,10)if i!=2])
print(permut[999999-725760])# since [1000000-1]-[725761-1] (2 _ _.. starts from 725761 but list starts at 0 )        
