#md5-iden-2byte
#g4 P02
#Nathaniel Law

import sys
import hashlib
import struct

max = 65535
        
for i in range(0, max + 1):
    num = struct.pack('<H', i)
    a = hashlib.md5(num).hexdigest()[:4]
    b = a[:2]
    c = a[2:4]
    if int(c + b, 16) == i:
        print "Found one! " + str(i)
        print hashlib.md5(num).hexdigest()