'''
Question:

Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.
Let P be the product of these parts, P = r × r × ... × r = rk.

For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.

Let M(N) = Pmax for a given value of N.

It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which leads to Pmax = (11/4)4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.

However, for N = 8 the maximum is achieved by splitting it into three equal parts, so M(8) = 512/27, which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.

For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

Find ΣD(N) for 5 ≤ N ≤ 10000.'''


'''
Here, P(N,k)=(N/k)**k

After differentiating P with respect to k ,we get
dP/dk=P(ln(N/k)-1) [Implicit differentiation]

We can clearly see that P doesn't have a fixed minima
So the ciritical point must surely be a maxima

thus, putting dP/dk=0,
0=P(ln(N/k)-1)
ln(N/k)=1
Therefore,k=N/e

But we are separating k times(discrete,integer division)
But the rough calculation from critical point is close to the discrete maxima ,because the function is continuous and alteration by decimal places doesnt have lot of change.
For safety, we round both up and down and check for maxima
-------------------------------------------------------------------------
For checking if terminating or not,we know if prime factorisation of denominator yields numbers other than 2 or 5 , it is non terminating eg:11/3
'''
from fractions import Fraction
from math import ceil,floor,e,log
P=lambda N,k:k * log(N / k)# calculating (n/k)**k is too slow, so instead use log.

def checker(n):
    if n==1:return True
    if n%2==0: return checker(n/2)
    if n%5==0: return checker(n/5)
    return False
counter=0
for i in range(5,10001):
    k=i/e
    up,down=ceil(k),floor(k)
    up_frac,down_frac=P(i,up),P(i,down)
    if up_frac>down_frac:
        denominator=Fraction(i,up).denominator
    else:
        denominator=Fraction(i,down).denominator
    if checker(denominator):
        counter-=i
    else:
        counter+=i
print(counter)
        
