step =26
ss ='The die is cast'

def CzEncrypt(char, step):
    step = step%26
    ordx = ord(char) + step
    if ord('A') <= ord(char) <=ord('Z'):
        if ordx > ord('Z'):
            return(chr(ordx-26))
        else:
            return(chr(ordx))
    elif ord('a') <= ord(char) <=ord('z'):
        if ordx > ord('z'):
            return(chr(ordx-26))
        else:
            return(chr(ordx))    
    else:
        return char
        
for s in ss:
    print(CzEncrypt(s,step), end='')
