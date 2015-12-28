#!/usr/bin/python
import isa
import os,sys,re
f = open(sys.argv[1],"r")
lines = f.readlines()
out = open(sys.argv[2],"wb")
label_pattern = re.compile(r"^.*:") #matches a label
arr = []

byte_counter = 0
for line in lines:
    line = re.sub(r"\;.*","",line)
    line = line.strip()
    if line:
        tokens = re.split(r"[ ,]",line)
        
        if label_pattern.match(tokens[0]):
            label = tokens[0][:-1]
            print "label: " + label + " at: " + str(byte_counter)
            isa.labels[label] = byte_counter
            print isa.labels
            tokens.pop(0)
            if len(tokens) == 0:
                continue
        byte_counter += isa.getInstructionBytes(tokens)
  
for line in lines:
    line = re.sub(r"\;.*","",line)
    line = line.strip()
    if line:
        tokens = re.split(r"[ ,]",line)
        if label_pattern.match(tokens[0]):
            tokens.pop(0)
            if len(tokens) == 0:
                continue
        ret = isa.decodeInstruction(tokens)
        arr.extend(ret)
print arr
byte_array = bytearray(arr)
out.write(byte_array)
