# 埃拉托色尼筛选

import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primeSieve(SieveSize):
    sieve = [True] * SieveSize
    sieve[0] = False
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(SieveSize)) + 1):
        pointer = i * 2
        while pointer < SieveSize:
            sieve[pointer] = False
            pointer += i

    # compile the list of prime
    primes = []
    for i in range(SieveSize):
        if sieve[i] == True:
            prime.append(i)

    return primes