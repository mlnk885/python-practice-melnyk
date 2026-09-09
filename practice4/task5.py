d = 2
c = 6

print("Diana Melnyk, I-23")

n = d * c

print(f"n = {d} * {c} = {n}")

# Divisors
divisors = []
divisor_sum = 0

for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)
        divisor_sum += number

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisor_sum}")

# Check if n is prime
if n < 2:
    is_prime = False
else:
    for number in range(2, n):
        if n % number == 0:
            is_prime = False
            break
    else:
        is_prime = True

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

# All prime numbers from 2 to n
primes = []

for number in range(2, n + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        primes.append(number)

print("Primes up to", n, ":", *primes)
print(f"Primes count: {len(primes)}")