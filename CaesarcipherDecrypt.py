#CaesarCipher-Decrypt

import string
from keylib import *

alphabet = string.ascii_uppercase

Maximum_KeySize = len(alphabet)

def getTranslatedMessage(message, key):
    translated = ''
    #for each char letter in string message
    for letter in message:
        #False for decryption
        translated += shift(letter, key, False)

    return translated
'''
#gets input from commmand line
line = input()

#key = first value in line
key = int(line[0])

#text to be decrypted = second value in line
text = line[1]

#changing key to be between 1 and 25
# for example: key = 100, changed key = 22
if key > Maximum_KeySize:
    key = key % Maximum_KeySize
    if key == 0:
        key += 1

#returns decrypted text
decryptedText =  getTranslatedMessage(text, key)
print decryptedText
'''
