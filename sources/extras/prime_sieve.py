# some prime numbers
# 11
# 101
# 1009
# 10007
# 100019
# 1000039
# 10000019
# 100000007
# 1000000007
# 10000000019
# 100000000003
# 1000000000061

# https://www.geeksforgeeks.org/python/python-program-to-print-all-prime-numbers-in-an-interval/
# start, end = 0, 1
start, end = 2, 11
primes = [True] * (end + 1)

# 0 and 1 are not prime
primes[0], primes[1] = False, False

for i in range(2, int(end ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, end + 1, i):
            primes[j] = False

res = [i for i in range(start, end + 1) if primes[i]]
print(res if res else "No")
