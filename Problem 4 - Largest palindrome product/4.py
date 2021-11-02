def largest_palindrome_returner(n=3):
    max_=0
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            prod=x*y
            prod_str=str(prod)
            if prod_str==prod_str[::-1] and prod>max_:
                max_=prod
    return max_
print(largest_palindrome_returner())
