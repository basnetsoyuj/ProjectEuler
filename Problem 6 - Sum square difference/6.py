sumofsq=sum([x*x for x in range(1,101)])
sqofsum=sum([x for x in range(1,101)])**2
print(abs(sumofsq-sqofsum))
