instructions = {
        "nop":0,
        "add":1,
        "sub":2,
        "out":3,
        "in":4,
        
        
        
        
        "push":128,
        }
def decodeInstruction(tokens):
    op = instructions[tokens[0]]
    if(op == 128):
        val = int(tokens[1])
        if(val>= 1<<14):
            raise ValueError("Value "+str(val) +" is too large to encode")
        l = []
        l.append(128 + ((val>>8)&63))
        l.append(val & 255)
        return l
    return [op]
