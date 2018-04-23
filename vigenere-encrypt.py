#Callum Walsh
import sys

# Did they give me a key?
if len(sys.argv) <= 1:
  print "I need a key"
  sys.exit(1)

key = int(sys.argv[1])

text = ""

if len(sys.argv) == 2:
  # Just a key given, need to get info from stdin
  text = sys.stdin.read()
else:
  # filename given, read from the given file
  file = open(sys.argv[2])
  text = file.read()
  file.close()

for i in range(len(text)):
  #print text[i], " ", ord(text[i])
  if ord(text[i]) >= 65 and ord(text[i]) <= 90:
    #upper!
    sys.stdout.write(chr( ((ord(text[i]) - ord('A')) + key) % 26 + ord('A')))
  elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
    #lowers!
    sys.stdout.write( chr( ((ord(text[i]) - ord('a')) + key) % 26 + ord('a')) )
  else:
    sys.stdout.write( text[i] )