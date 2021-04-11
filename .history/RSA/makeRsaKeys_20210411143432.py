import random, sys, os, cryptomath
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
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print('Calculating d that is mod inverse of e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publickey = (n, e)
    privatekey = (n, d)

    print('Public key:', publickey)
    print('Private key:', privatekey)

    return (publickey, privatekey)
