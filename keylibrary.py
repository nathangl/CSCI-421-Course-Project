import string
import sys
from string import letters, digits
from random import shuffle

monoalpha_cipher = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ': ' ',
}

#command line input
def input():
    if len(sys.argv) <= 1:
        print "I need a key!"
        sys.exit(1)
    
    if len(sys.argv) == 2:
        text = sys.stdin.read()
        text = text.replace('\n', ' ').replace('\r', '')
    else:
        with open(sys.argv[2]) as file:
            text = file.read()
            text = text.replace('\n', ' ').replace('\r', '')
    
    return (sys.argv[1], text)
        
#MONOALPHABETIC  -------------------------------------------------------
#FUNCTIONS -------------------------------------------------------
        
def random_monoalpha_cipher(pool=None):
    """Generate a Monoalphabetic Cipher"""
    if pool is None:
        pool = letters + digits
    original_pool = list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))

def inverse_monoalpha_cipher(monoalpha_cipher):
    """Given a Monoalphabetic Cipher (dictionary) return the inverse."""
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.iteritems():
        inverse_monoalpha[value] = key
    return inverse_monoalpha

def encrypt_with_monoalpha(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
    return encrypt_with_monoalpha(
               encrypted_message,
               inverse_monoalpha_cipher(monoalpha_cipher)
           )