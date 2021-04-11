# 埃拉托色尼筛选

import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def primeSieve(SieveSize):
    sieve = [True] * SieveSize
    sieve[0] = False
    sieve[1] = False