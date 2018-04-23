#md5-iden-3byte
#g4 P02
#Anca-Maria Murgoci and Nathaniel Law

import sys
import hashlib
import struct

max = 16777215

for i in range(0, max + 1):
    num = struct.pack('<I', i)
    a = hashlib.md5(num[0:3]).hexdigest()
    #switch order of hex to convert to decimal... couldn't figure out how to unpack properly
    b = a[:2]
    c = a[2] + a[3]
    d = a[4] + a[5]
    e = d + c + b
    
    if int(e, 16) == i:
        print "Found one! " + str(i)
        print hashlib.md5(num[0:3]).hexdigest()