import isa
import os,sys,re
f = open(sys.argv[1],"r")
out = open(sys.argv[2],"wb")
arr = []
for line in f:
    line = re.sub(r"\;.*","",line)
    line = line.strip()
    if line:
        tokens = re.split(r"[ ,]",line)
        ret = isa.decodeInstruction(tokens)
        arr.extend(ret)
print arr
byte_array = bytearray(arr)
out.write(byte_array)
