import sys
import struct
l = []
for a in sys.argv[1:]:
    for part in a.split(","):
        if part.strip():
            l.append(int(part.strip()))
l = bytearray(l)
print(struct.unpack('<%df' % (len(l) / 4), l))
