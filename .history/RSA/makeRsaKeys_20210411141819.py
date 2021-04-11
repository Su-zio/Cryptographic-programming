import random, sys, os, Cryptodome.Math
from Prime import rabinMiller


def main():
    print('Makeing key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('key files made...')


def generateKey(keySize):
    print('Generating p prime...')
    p = rabinMiller.generateLargerPrime(keySize)
