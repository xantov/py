step =27
ss ='The die is cast'

def CzEncrypt(char, step):
    step = step%26
    ordx = ord(char) + step
    val = ''
    if ord('A') <= ord(char) <=ord('Z'):
        val = chr(ordx-26) if ordx > ord('Z') else chr(ordx)
    elif ord('a') <= ord(char) <=ord('z'):
        val = chr(ordx-26) if ordx > ord('z') else chr(ordx)
    else:
        val = char
    return val

for s in ss:
    print(CzEncrypt(s,step), end='')
