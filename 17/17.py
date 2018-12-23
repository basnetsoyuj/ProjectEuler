import converter
sum_=0
for x in range(1,1001):
    string=converter.converter(x).replace(" ",'')
    sum_+=len(string)
print(sum_)
