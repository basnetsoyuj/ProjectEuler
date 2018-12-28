def value(str_):
    list_=list(str_)
    sum_=0
    for alphabet in list_:
        sum_+=ord(alphabet)-64
    return sum_
triangle_nums={int(n*(n+1)*0.5) for n in range(0,80)}
with open('p042_words.txt','r') as file:
    total=0
    words_list=file.read()[1:-1].split('","')
    for word in words_list:
        value_=value(word)
        if value_ in triangle_nums:total+=1
    print(total)
