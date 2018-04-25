import string
import sys

#shifts letter by nr, direction is a bool: True for forward, False for backward
#Example: 'A', 1, True will return B --------- 'A', 1, False will return Z
def shift(letter, nr, direction):
    #letter = letter.upper()
    uAlphabet = string.ascii_uppercase
    lAlphabet = string.ascii_lowercase
    if direction:
        try:
            try:
                return lAlphabet[(lAlphabet.index(letter) + nr) % len(lAlphabet)]
            except:
                return uAlphabet[(uAlphabet.index(letter) + nr) % len(uAlphabet)]
        except:
            return letter
    else:
        try:
            try:
                return lAlphabet[(lAlphabet.index(letter) - nr) % len(lAlphabet)]
            except:
                return uAlphabet[(uAlphabet.index(letter) - nr) % len(uAlphabet)]
        except:
            return letter

def getEncryptedCaesarMessage(message, key):
    translated = ''
    #for each char letter in string message
    for letter in message:
        #True for encryption
        translated += shift(letter, key, True)

    return translated

def getDecryptedCaesarMessage(message, key):
    translated = ''
    #for each char letter in string message
    for letter in message:
        #False for decryption
        translated += shift(letter, key, False)

    return translated

#Vignere
def getEncryptedVignereMessage(text, key):
    curkey = ord(key[0]) - ord('a') + 1
    finalText = ''
    for i in range(len(text)):
       #print text[i], " ", ord(text[i])
       #print curkey
       if ord(text[i]) >= 65 and ord(text[i]) <= 90:
         #upper!
         finalText += chr( ((ord(text[i]) - ord('A')) + curkey) % 26 + ord('A'))
         # update curkey
         curkey = ord(key[ (i+1) % len(key) ]) - ord('a') + 1
       elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
         #lowers!
         finalText += chr( ((ord(text[i]) - ord('a')) + curkey) % 26 + ord('a'))
         # update curkey
         curkey = ord(key[(i+1) % len(key)]) - ord('a') + 1
       else:
         finalText += text[i]
    return finalText

def getDecryptedVignereMessage(text, key):
    curkey = ord(key[0]) - ord('a') + 1
    finalText = ''
    for i in range(len(text)):
       #print text[i], " ", ord(text[i])
       #print curkey
       if ord(text[i]) >= 65 and ord(text[i]) <= 90:
         #upper!
         finalText += chr( ((ord(text[i]) - ord('A')) - curkey + 26) % 26 + ord('A'))
         # update curkey
         curkey = ord(key[ (i+1) % len(key) ]) - ord('a') + 1
       elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
         #lowers!
         finalText += chr( ((ord(text[i]) - ord('a')) - curkey + 26) % 26 + ord('a'))
         # update curkey
         curkey = ord(key[(i+1) % len(key)]) - ord('a') + 1
       else:
         finalText += text[i]
    return finalText

#PLAYFAIR  -------------------------------------------------------
#FUNCTIONS -------------------------------------------------------

#returns encrypted message using playfair
def getEncryptedPlayfairMessage(text, key):
    key = playKey(key)
    matrix = playMatrix(key)
    pairs = playPairs(text)
    encrypt = playEncrypt(matrix, pairs)

    finalText = ''
    for pair in encrypt:
        finalText += pair + ' '

    return finalText

def getDecryptedPlayfairMessage(text, key):
    key = playKey(key)
    matrix = playMatrix(key)
    pairs = playPairs(text)
    encrypt = playDecrypt(matrix, pairs)

    finalText = ''
    for pair in encrypt:
        finalText += pair + ' '

    return finalText

#returns the changed key for playfair
def playKey(keyT):
    keyT = keyT.upper()
    keyT = keyT.replace("J", "")    #remove Js
    keyT = ''.join(sorted(set(keyT), key=keyT.index))  #remove repeats

    return keyT

#returns the changed text for playfair
def playPairs(text):
    text = text.translate(None, string.punctuation)    #removes punctuation
    text = text.replace(" ", "")   #removes spaces
    text = text.upper() #changes string to uppcase
    text = text.replace("J", "I")   #replaces J with I

    #split string into pairs
    n = 2
    pairs = [text[i:i+n] for i in range(0, len(text), n)]

    #pad with X
    if len(pairs[len(pairs) - 1]) == 1:
        pairs[len(pairs) - 1] = pairs[len(pairs) - 1] + 'X'

    #replace duplicate pairs with X
    for index, pair in enumerate(pairs):
        if pair[0] == pair[1]:
            pairs[index] = pair[0] + 'X'

    return pairs

def playMatrix(key):
    matrix = []
    uAlphabet = string.ascii_uppercase
    uAlphabet = uAlphabet.replace("J", "")

    #create array
    for x in key:
        matrix.append(x)
    for z in uAlphabet:
        if z in matrix:
            continue
        else:
            matrix.append(z)

    return matrix

def playEncrypt(matrix, pairs):
    for i, x in enumerate(pairs):
        #x is ['A', 'B']
        index = pairs.index(x)
        fIndex = matrix.index(x[0]) #find index of each in matrix
        sIndex = matrix.index(x[1])
        first = (fIndex % 5, fIndex / 5)    #new [col#, row#]
        second = (sIndex % 5, sIndex / 5)

        #same column
        if first[0] == second[0]:
            x = matrix[(((first[1] + 1) % 5) * 5) + first[0]]
            x += matrix[(((second[1] + 1) % 5) * 5) + second[0]]
        #same row
        elif first[1] == second[1]:
            x = matrix[(first[1] * 5) + ((first[0] + 1) % 5)]
            x += matrix[(second[1] * 5) + ((second[0] + 1) % 5)]
        #diff
        else:
             x = matrix[(first[1] * 5) + second[0]]
             x += matrix[(second[1] * 5) + first[0]]
        pairs[i] = x
    return pairs

def playDecrypt(matrix, pairs):
    for i, x in enumerate(pairs):
        #x is ['A', 'B']
        index = pairs.index(x)
        fIndex = matrix.index(x[0]) #find index of each in matrix
        sIndex = matrix.index(x[1])
        first = (fIndex % 5, fIndex / 5)    #new [col#, row#]
        second = (sIndex % 5, sIndex / 5)

        #same column
        if first[0] == second[0]:
            x = matrix[(((first[1] - 1) % 5) * 5) + first[0]]
            x += matrix[(((second[1] - 1) % 5) * 5) + second[0]]
        #same row
        elif first[1] == second[1]:
            x = matrix[(first[1] * 5) + ((first[0] - 1) % 5)]
            x += matrix[(second[1] * 5) + ((second[0] - 1) % 5)]
        #diff
        else:
             x = matrix[(first[1] * 5) + second[0]]
             x += matrix[(second[1] * 5) + first[0]]
        pairs[i] = x
    return pairs
