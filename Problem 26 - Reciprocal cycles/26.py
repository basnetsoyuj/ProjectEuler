X = 1000

max_recurring_digits = 0
max_num = 0

for i in range(2, 1000):
  # skip multiples of 2 and 5; they are terminating as 2 & 5 are factors of 10 (any decimal number)
  if i % 2 and i % 5:
    n = 1
    n_digits = 0
    while True:
      # 1 is smaller than all divisors, so 0 is added at the end in each step while dividing number in decimal places
      n *= 10

      # make the remainder the new dividend
      n = n % i

      # since we are computing 1/d, our initial divided is 1
      # so the state when digits starts recurring is:
      # when the remainder is our initial dividend i.e. 1
      if n == 1:
        break
      n_digits +=1

    if n_digits > max_recurring_digits:
      max_num = i
      max_recurring_digits = n_digits

print(max_num)