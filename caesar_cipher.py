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

def CzDecrypt(char, step):
    # step = step%26
    ordx = ord(char) + 26 - step
    val = ''
    if ord('A') <= ordx <= ord('Z') or ord('a') <= ordx <= ord('z'):
        val = chr(ordx)
    elif ordx > 63:
        val = chr(ordx-26)
    else:
        val = char
    return val

#TEST
step =27

ec ='The Caesar cipher is named after Julius Caesar..'
print('Encryped text: ',end='')
for e in ec:
    print(CzEncrypt(e,step),end='')

dc='Uif Dbftbs djqifs jt obnfe bgufs Kvmjvt Dbftbs..'
print('\nDecrypted text: ',end='')
for x in dc:
    print(CzDecrypt(x,step),end='')
