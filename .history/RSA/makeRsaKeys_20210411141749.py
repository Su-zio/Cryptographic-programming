import random, sys, os, Prime.rabinMiller, Cryptodome.Math


def main():
    print('Makeing key files...')
    makeKeyFiles('al_sweigart', 1024)
    print('key files made...')


def generateKey(keySize):
    print('Generating p prime...')
    p = rabinMiller.generateLargerPrime(keySize)
