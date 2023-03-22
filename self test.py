import field
from tinyec import registry
# Curve brainpoolP256r1
dA =b'81DB1EE100150FF2EA338D708271BE38300CB54241D79950F77B063039804F1D'

x_qA =b'44106E913F92BC02A1705D9953A8414DB95E1AAA49E81D9E85F929A8E3100BE5'
y_qA =b'8AB4846F11CACCB73CE49CBDD120F5A900A69FD32C272223F789EF10EB089BDC'

dB =b'55E40BC41E37E3E2AD25C3C6654511FFA8474A91A0032087593852D3E7D76BD3'

x_qB =b'8D2D688C6CF93E1160AD04CC4429117DC2C41825E1E9FCA0ADDD34E6F1B39F7B'
y_qB =b'990C57520812BE512641E47034832106BC7D3E8DD0E4C7F1136D7006547CEC6A'

x_Z =b'89AFC39D41D3B327814B80940B042590F96556EC91E6AE7939BCE31F3A18BF2B'
y_Z =b'49C27868F4ECA2179BFD7D59B1E3BF34C1DBDE61AE12931648F43E59632504DE'

samplecurve = registry.get_curve("brainpoolP256r1")
curve = field.Curve(samplecurve.a, samplecurve.b, samplecurve.field.p, samplecurve.field.n, samplecurve.g.x, samplecurve.g.y)
x1 = int(x_qA, 16)
y1 = int(y_qA, 16)
x2 = int(x_qB, 16)
y2 = int(y_qB, 16)
x3 = int(x_Z, 16)
y3 = int(y_Z, 16)

priKey1 = int(dA, 16)
priKey2 = int(dB, 16)
pubKey1 = field.Point(curve, x1, y1)
pubKey2 = field.Point(curve, x2, y2)
masterKey = field.Point(curve, x3, y3)

# print(curve.on_curve(x1,y1))
# print(curve.on_curve(x2,y2))
# print(curve.on_curve(x3,y3))

test_add = pubKey1 + pubKey1 + pubKey1
test_mul = 2 * pubKey1 + pubKey1
test = pubKey1 * 3
print("p = ", curve.p)
print("a = ", curve.a)
print("b = ", curve.b)
print("Xp = ", x1)
print("Yp = ", y1)
print("test x = ", test.x)
print("test y = ", test.y)
print("test_add x =", test_add.x)
print("test_add y =", test_add.y)
print("test_mul x =", test_mul.x)
print("test_mul y =", test_mul.y)

