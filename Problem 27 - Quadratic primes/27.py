A = 1000
B = 1000

a = b = 0

function = lambda n: n**2 + a*n + b

max_ = 0
product = 0

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if not n % i:
      return False
  return True

# since (function) generates prime for n=0, b must be prime
for b in range(B):
  if is_prime(b):
    for a in range(-A+1, A):
      n = 0
      counter = 0
      while True:
        if not is_prime(function(n)):
          if counter > max_:
            product = a*b
            max_ = counter
          break
        counter += 1
        n += 1

print(product)