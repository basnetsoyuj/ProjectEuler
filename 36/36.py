sum_=0
for x in range(1,1000000):
    b10=str(x)
    b2=str(bin(x))[2:]
    if b10==b10[::-1] and b2==b2[::-1]:
        sum_+=x
print(sum_)
