import sys
import hashlib

max = 65535
#65535
#16777215

for i in range(0, max + 1):
    m = hashlib.md5()
    m.update(str(i))
    byte = m.hexdigest()[:4], 16
    if int(m.hexdigest()[:4], 16) == i:
        print "Found one! " + str(i)
    