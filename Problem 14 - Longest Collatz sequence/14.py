from itertools import islice,count
memoizer={}
max_=(0,0)
for x in islice(count(1),1000000):
    num=x
    seqlen=0
    while num!=1:
        if num in memoizer:
            seqlen+=memoizer[num]
            break
        seqlen+=1
        if num%2==0:
            num=num/2
        else:
            num=3*num+1
    memoizer[x]=seqlen
    if seqlen>max_[1]:
        max_=(x,seqlen)
print("Number :",max_[0],",Sequence length :",max_[1])