#Callum Walsh
#xor.py
#g4 P02
import sys


# Did they give me a key?
if len(sys.argv) != 4: 
  print "Must specify an input file."
  sys.exit(1)
 
inputFile =(sys.argv[1]) 
key = (sys.argv[2])
outputFile = sys.argv[3]
i = 0

with open(inputFile, "rg") as fin:
 with open(outputFile, "wb") as fout:
  byte = fin.read(1)
  while byte:
    fout.write(chr(ord(byte) ^ ord(key[i % len(key)] ) ) )
    byte = fin.read(1)
    i = i + 1
    