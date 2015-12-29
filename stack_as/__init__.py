#!/usr/bin/python
import isa
import os,sys,re
def main(lines):
    
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
                
                isa.labels[label] = byte_counter
                
                tokens.pop(0)
                if len(tokens) == 0:
                    continue
            byte_counter += isa.getInstructionBytes(tokens,byte_counter)
  
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
    #print arr
    return arr
    
def cmdline():
    if len(sys.argv) != 3:
        print "Usage: stack_as [asm.s] [outfile]"
        sys.exit(1)
    f = open(sys.argv[1],"r")
    lines = f.readlines()
    out = open(sys.argv[2],"wb")
    arr = main(lines)
    byte_array = bytearray(arr)
    out.write(byte_array)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: stack_as [asm.s] [outfile]"
        sys.exit(1)
    f = open(sys.argv[1],"r")
    lines = f.readlines()
    out = open(sys.argv[2],"wb")
    arr = main(lines)
    byte_array = bytearray(arr)
    out.write(byte_array)
