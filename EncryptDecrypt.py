from tinyec import registry
from tinyec import ec
from math import sqrt
import secrets, binascii

curve = registry.get_curve("brainpoolP256r1")
h = curve.field.h
a = curve.a
b = curve.b
n = curve.field.n
p = curve.field.p
coef = 50

def checkSquare(n):
    upbound = n
    lowbound = 0
    root = n
    while True:
        root = int((upbound + lowbound) / 2)
        if (root * root == n):
            return True
        elif (root * root > n):
            lowbound = upbound
            upbound = root
        else:
            upbound = lowbound
            lowbound = root

        if upbound == lowbound :
            return False  
        
def encodeMsg(msg):
    x = coef * msg
    for _ in range(coef):
        y_square = (x*x*x + a*x + b) % p
        if (checkSquare(y_square)):
            point = ec.Point(curve, x, sqrt(y_square))
            return point
        x += 1

def decodeMsg(decryptedMsg):
    P1, P2 = decryptedMsg
    msg = P1 / coef
    return msg

def encrypt_ECC(msg, pubKey):
    msg = encodeMsg(msg)
    k = secrets.randbelow(curve.field.n)
    P1 = k * curve.field.g
    P2 = msg + k * pubKey
    return P1, P2

def decrypt_ECC(encryptedMsg, privKey):
    P1, P2 = encryptedMsg
    decryptedMsg = P2 - privKey * P1
    msg = decodeMsg(decryptedMsg)
    return msg

msg = b"khanh rat dep trai"
print("original msg:", msg)

hexMsg = binascii.hexlify(msg)
print("hex msg:", hexMsg)

decMsg = int(hexMsg, 16)
print("dec msg:", decMsg)

print("a = ", a)
print("b = ", b)
print("p = ", p)
print("n = ", n)
encode = encodeMsg(decMsg)
print("Encoded msg: ", encode)
# privKey = secrets.randbelow(curve.field.n)
# pubKey = privKey * curve.g

# print("Private key: ", privKey)
# print("Public key", pubKey)

# encryptedMsg = encrypt_ECC(decMsg, pubKey)
# print(encryptedMsg)
# decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
# print(decryptedMsg)





