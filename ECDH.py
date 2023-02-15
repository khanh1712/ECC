from tinyec import registry
from tinyec import ec
import secrets

curve = registry.get_curve("brainpoolP256r1")

p = curve.field.p
n = curve.field.n
g = curve.g

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def calcPubKey(priKey):
    pubKey = priKey * g
    return pubKey

def calcSSK(selfPriKey, receivedPubKey):
    ssk = selfPriKey * receivedPubKey
    return ssk

priKey = secrets.randbelow(n)
cipherPriKey = secrets.randbelow(n)
receivedPubKey = calcPubKey(cipherPriKey)

print("Private key: ", hex(priKey))
print("Received public key: ", compress_point(receivedPubKey))

ssk = calcSSK(priKey, receivedPubKey)
print("Session Key: ", compress_point(ssk))
