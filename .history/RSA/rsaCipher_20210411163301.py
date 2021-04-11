import sys

DEFAULT_BLOCK_SIZE = 128 # 128 bytes

BYTE_SIZE = 256 # One byte has 256 different values.

def main():
    filename = 'encrypted_file.txt' # the file to write to/read from
    mode = 'encrypt' # set to 'encrypt' or 'decrypt'
    
    if mode == 'encrypt':  
        message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
        pubKeyFilename = 'al_sweigart_pubkey.txt'
        print('Encrypting and writing to %s...' % (filename))
        encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)
        print('Encrypted text:')
        print(encryptedText)
        
    elif mode == 'decrypt':
        privKeyFilename = 'al_sweigart_privkey.txt'
        print('Reading from %s and decrypting...' % (filename))
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
        print('Decrypted text:')
        print(decryptedText)

def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    messageBytes = message.encode('ascii') # convert the string to bytes
    blockInts = []

    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):

    # Converts a list of block integers to the original message string.

      # The original message length is needed to properly convert the last

     # block integer.

     message = []

     for blockInt in blockInts:

         blockMessage = []

         for i in range(blockSize - 1, -1, -1):

             if len(message) + i < messageLength:

                 # Decode the message string for the 128 (or whatever

                 # blockSize is set to) characters from this block integer.

                asciiNumber = blockInt // (BYTE_SIZE ** i)

                 blockInt = blockInt % (BYTE_SIZE ** i)

                 blockMessage.insert(0, chr(asciiNumber))

   message.extend(blockMessage)

   return ''.join(message)



def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):


encryptedBlocks = []

  n, e = key



 for block in getBlocksFromText(message, blockSize):

      # ciphertext = plaintext ^ e mod n

       encryptedBlocks.append(pow(block, e, n))

   return encryptedBlocks



def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):


   decryptedBlocks = []

     n, d = key

   for block in encryptedBlocks:

        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))

    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)



 94. def readKeyFile(keyFilename):



   fo = open(keyFilename)

    content = fo.read()

    fo.close()

     keySize, n, EorD = content.split(',')

    return (int(keySize), int(n), int(EorD))





 def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):



   keySize, n, e = readKeyFile(keyFilename)



   if keySize < blockSize * 8: # * 8 to convert bytes to bits

    sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))



     encryptedBlocks = encryptMessage(message, (n, e), blockSize)




 for i in range(len(encryptedBlocks)):

         encryptedBlocks[i] = str(encryptedBlocks[i])

     encryptedContent = ','.join(encryptedBlocks)



    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)

   fo = open(messageFilename, 'w')

     fo.write(encryptedContent)

    fo.close()

    # Also return the encrypted string.

     return encryptedContent





 def readFromFileAndDecrypt(messageFilename, keyFilename):

   # Using a key from a key file, read an encrypted message from a file

    # and then decrypt it. Returns the decrypted message string.

     keySize, n, d = readKeyFile(keyFilename)



    # Read in the message length and the encrypted message from the file.

    fo = open(messageFilename)

    content = fo.read()

    messageLength, blockSize, encryptedMessage = content.split('_')

    messageLength = int(messageLength)

    blockSize = int(blockSize)



  # Check that key size is greater than block size.

   if keySize < blockSize * 8: # * 8 to convert bytes to bits

     sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))



   # Convert the encrypted message into large int values.

  encryptedBlocks = []

   for block in encryptedMessage.split(','):

     encryptedBlocks.append(int(block))



 # Decrypt the large int values.

 return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)



# If rsaCipher.py is run (instead of imported as a module) call

 # the main() function.

if __name__ == '__main__':

    main()