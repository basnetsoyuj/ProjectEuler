# here the side n has 2n steps from origin to end irrespective of the order ,it has n for right n for down(only two options)
# and thus the number of was n items can be chosen from 2n items is C(2n,n)
from math import factorial
side=20
print(int(factorial(2*side)/(factorial(side)**2)))