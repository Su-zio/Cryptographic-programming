import random, sys, os
import cryptomath,rabinMiller



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


def makeKeyFiles(name, keySize):
    if os.path.exists('%spubkey.txt' %
                      (name)) or os.path.exists('%sprivkey.txt' % (name)):
        sys.exit(
            'WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.'
            % (name, name))
    publickey, privatekey = generateKey(keySize)

    print()

    print('The public key is a %s and a %s digit number.' %
          (len(str(publickey[0])), len(str(publickey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publickey[0], publickey[1]))
    fo.close()

    print()

    print('The private key is a %s and a %s digit number.' %
          (len(str(privatekey[0])), len(str(privatekey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privatekey[0], privatekey[1]))
    fo.close()


if __name__ == '__main__':
    main()