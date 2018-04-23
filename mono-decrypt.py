# This is an decrypted plain text using  monoalphabetic cipher code

import random
import string
from keylibrary import *


#alphabet = string.ascii_letters
line = input()
key = line[0]
encrypted = line[1]

encrypted = encrypted.lower()

random_monoalpha_cipher(pool=None)
inverse = inverse_monoalpha_cipher(monoalpha_cipher)
decrypted = decrypt_with_monoalpha(encrypted, monoalpha_cipher)


print(decrypted)