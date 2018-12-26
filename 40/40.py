digits=['0','1','2','3','4','5','6','7','8','9']
str_="123456789"
n=1
end=1000000
while len(str_)<end:
    for x in digits:
        str_+=str(n)+str(x)
    n+=1
n=1
product=1
while n<=end:
    product*=int(str_[n-1])
    n*=10
print(product)
    
