instructions = {
        "nop":0,
        "add":1,
        "sub":2,
        "out":3,
        "in":4,
        "dup":5,
        "drop":6,
        "swap":7,
        "rot":8,
        
        "jump":32,
        "cjump":64+32,
        "push":128,
        }
labels = {}
byte_counter = 0
def decodeInstruction(tokens):
    global byte_counter
    global labels
    byte_counter += getInstructionBytes(tokens)
    op = instructions[tokens[0]]
    if(op == 128):
        val = 0
        val = int(tokens[1])
        if(val>= 1<<14):
            raise ValueError("Value "+str(val) +" is too large to encode")
        l = []
        l.append(128 + ((val>>8)&127))
        l.append(val & 255)
        return l
    elif(op == 32 or op == 96):
        print tokens[1] 
        if tokens[1] in labels:
            val = labels[tokens[1]]- byte_counter
        else:
            val = int(tokens[1])
        if(val>= 1<<12):
            raise ValueError("Value "+str(val) +" is too large to encode")
        l = []
        l.append(op + ((val>>8)&31))
        l.append(val & 255)
        return l
    
    return [op]
def getInstructionBytes(tokens):
    op = instructions[tokens[0]]
    if(op > 31):
        return 2
    return 1
