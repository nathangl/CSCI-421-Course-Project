#Callum Walsh
#Vigenere Encryption and decryption.
import sys
'''
# Did they give me a key?
if len(sys.argv) <= 1:
  print "I need a key"
  sys.exit(1)

#print sys.argv

#key = int(sys.argv[2])#stores key in approriate array.
key = sys.argv[1]
#line ten needs changing I think so that the text can shift N1 way and N2 ways
# if enter 1 and 2 then it will only accept 1 [test.py, 1 , 2]
#key2 is a test. need to implement something in for loop

text = ""



#line 19 how many can be in the array
if len(sys.argv) == 2:
  # Just a key given, need to get info from stdin

  text = sys.stdin.read()

  #Line 23 text = ..... stores the word provided on the command line

else:
  # filename given, read from the given file
  file = open(sys.argv[2])
  text = file.read()

  file.close()
'''

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
