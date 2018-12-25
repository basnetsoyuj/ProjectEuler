def value(str_):
    list_=list(str_)
    sum_=0
    for alphabet in list_:
        sum_+=ord(alphabet)-64
    return sum_
with open("names.txt",'r') as file:
    list_=file.read().replace("\"",'').split(",")
    list_.sort()
    sum_=0
    for x in range(0,len(list_)):
        sum_+=value(list_[x])*(x+1)
print(sum_)
