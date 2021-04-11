import random, sys, os, Cryptodome.Math
from Prime import rabinMiller


def main():
    print('Makeing key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('key files made...')


def generateKey(keySize):
    print('Generating p prime...')
    p = rabinMiller.generateLargerPrime(keySize)
    print('Generating q prime...')
    q = rabinMiller.generateLargerPrime(keySize)
    n = p * q

    print('Generating e that is relatively prime to(p-1)*(q-1)...')
    while True:
        e = random.randrange(2**(keySize - 1), 2**(keySize))
        if Cryptodome.Math.gcd(e, (p - 1) * (q - 1)) == 1:
            break
