# This is an encrypted plain text using  monoalphabetic cipher code

import random
import string
from keylibrary import *


#alphabet = string.ascii_letters
line = input()
key = line[0]
plaintext = line[1]

plaintext = plaintext.lower()

random_monoalpha_cipher(pool=None)
inverse = inverse_monoalpha_cipher(monoalpha_cipher)
encrypted = encrypt_with_monoalpha(plaintext, monoalpha_cipher)


print(encrypted)

       