distinct=set()
for a in range(2,101):
    for b in range(2,101):
        distinct.add(a**b)
print(len(distinct))
