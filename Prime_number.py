def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Loop through numbers 2 to 100 and print primes
for num in range(2, 101):
    if is_prime(num):
        print(num, end=" ") 
        
print()