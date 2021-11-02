# inclusive upper bound; less than 2000000 in question
X = 2000000 - 1

seen = set()
sum_ = 0

# similar to a prime seive
# for loop to add all the composite numbers
for i in range(2, X + 1):
    if i not in seen:
        # start with the 2nd multiple of the number
        n = 2 * i
        while n < X + 1:
            if n not in seen:
                # add all the multiples
                sum_ += n
                seen.add(n)
            n += i
            
# (sum of all primes) = (the total sum of all numbers till X) - (sum of all composite numbers)
# -1 since 1 is not included in the loop
print(X*(X+1)/2 - sum_ - 1)
