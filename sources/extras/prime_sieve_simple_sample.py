# Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
def prime_list_by_sieve(number):
    if number < 2:
        return []

    # All number from 0 - number are hold in a list
    # Advantage: the index is identical with the associated number
    # The value of each element in the list is True (prime) or
    # False (not a prime).
    # At the begin all elements are set to True and then, step by
    # step, set to False, if the number is not a prime.

    # Init primes sieve: all numbers marked as primes
    prime_sieve = [True] * (number + 1)

    # 0 and 1 aren't primes: mark them as False
    prime_sieve[0] = False
    prime_sieve[1] = False

    for idx in range(2, number + 1):
        if not prime_sieve[idx]:
            # Not a prime - nothing to do
            continue

        # prime_sieve[idx] is a prime - we can mark all
        # multiples of prime_sieve[idx] as False.
        multiplier = 2
        prod = multiplier * idx
        while prod <= number:
            prime_sieve[prod] = False
            multiplier += 1
            prod = multiplier * idx

    primes = [p for p, is_prime in enumerate(prime_sieve) if is_prime]
    return primes

print(prime_list_by_sieve(11))
# print(prime_list_by_sieve(101))
