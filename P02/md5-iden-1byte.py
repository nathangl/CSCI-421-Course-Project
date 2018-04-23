#md5-iden-1byte
#g4 P02
#Damilola Olakunle and Nathaniel Law

import sys
import hashlib
import struct

max = 255
        
for i in range(0, max + 1):
    num = struct.pack('<B', i)
    if int(hashlib.md5(num).hexdigest()[:2], 16) == i:
        print "Found one! " + str(i)
        print hashlib.md5(num).hexdigest()