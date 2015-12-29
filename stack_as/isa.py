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
        "ret":9,
        "lt":10,
        "eq":11,
        "gt":12,
        "neg":13,
        "rpush":14,
        "rpop":15,
        "rcp":16,
        "and":17,
        "or":18,
        "xor":19,
        "lshift":20,
        "rshift":21,
        "mul":22,
        "fetch":23,
        "store":24,
        "jump":32,
        "call":64,
        "cjump":64+32,
        "push":128,
        }
labels = {}
byte_counter = 0
def decodeInstruction(tokens):
    global byte_counter
    global labels
    l = []
    
    op = instructions[tokens[0]]
    if(op == 128):
        val = 0
        val = int(tokens[1])
        if(val>= 1<<14):
            raise ValueError("Value "+str(val) +" is too large to encode")
        
        if byte_counter % 2:
            #print "padded instruction"
            l.append(0)
        
        l.append(128 + ((val>>8)&63))
        l.append(val & 255)
        print val&255
        
    elif(op == 32 or op == 96 or op == 64):
        #print tokens[1] 
        if tokens[1] in labels:
            val = labels[tokens[1]]- (byte_counter+2)
        else:
            val = int(tokens[1])
        if(val>= 1<<12):
            raise ValueError("Value "+str(val) +" is too large to encode")
        
        if byte_counter % 2:
            #print "padded instruction"
            val -= 1
            l.append(0)
        l.append(op + ((val>>8)&31))
        l.append(val & 255)
    else:
        l.append(op)
    byte_counter += getInstructionBytes(tokens,byte_counter)    
    
    return l
def getInstructionBytes(tokens,byte_counter):
    
    op = instructions[tokens[0]]
    if(op > 31):
        if byte_counter %2:
            return 3
        return 2
    return 1
