#Nathaniel Law
#P01 Playfair decryption
import sys
from keylib import *

line = input()
key = line[0]
text = line[1]

key = playKey(key)
matrix = playMatrix(key)
pairs = playPairs(text)
encrypt = playDecrypt(matrix, pairs)

finalText = ''
for pair in encrypt:
    finalText += pair + ' '

print finalText