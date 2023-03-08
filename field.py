def inverseMod(d, n):
    t, newt = 0, 1
    r, newr = n, d
    
    while(newr != 0):
        q = r // newr
        r, newr = newr, (r % newr)
        t, newt = newt, (t - q*newt)
    if r > 1:
        print("not in vertible")
    else:
        if (t < 0):
            t += n
        return int(t)

class Curve(object):
    def __init__(self, p, a, b, x_g, y_g, n):
        self.p = p
        self.a = a
        self.b = b
        self.n = n
        self.g = Point(self, x_g, y_g)

    def on_curve(self, x, y):
        y_square = (y * y) % self.p 
        mod = (x * x * x + self.a * x + self.b) % self.p
        return y_square == mod
    
class Infinity(object):
    def __init__(self, curve, x = None, y = None):
        self.x = x
        self.y = y
        self.curve = curve
    
    def __add__(self, other):
        if isinstance(other, Point):
            return other
        if isinstance(other, Infinity):
            return Infinity()
    
    def __sub__(self, other):
        if isinstance(other, Point):
            return other
        if isinstance(other, Infinity):
            return Infinity()
    
class Point(object): 
    def __init__(self, curve, x, y): 
        self.x = x
        self.y = y
        self.curve = curve
    
    def __add__(self, other):
        # add infinity
        if isinstance(other, Infinity):
            return self
        # add a point
        elif self.curve == other.curve:
            x1 = self.x
            x2 = other.x
            y1 = self.y
            y2 = other.y
            a = self.curve.a
            p = self.curve.p
            # calculate lambda
            if x1 == x2 and y1 == y2:
                l = (3*x1*x1 + a) * inverseMod(2*y1, p) % p
            else:
                l = (y2 - y1) * inverseMod(x2 - x1, p) % p

            x3 = (l*l - x1 - x2) % p
            y3 = (l*(x1 - x3) - y1) % p
            return Point(self.curve, x3, y3)
            # if self.curve.on_curve(x3, y3):
            #     return Point(self.curve, x3, y3)
            # else:
            #     return Infinity(self.curve)
        else:
            raise ValueError("2 points on different curves")
        
    
    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ValueError("Not a point")
        other = Point(other.x, -other.y, other.curve)
        return self.__add__(other)
    
    def __mul__(self, times: int):
        if isinstance(times, int):
            if times >= self.curve.n:
                times -= self.curve.n
            if times == 0:
                return Infinity(self.curve)
            else:
                result = Infinity(self.curve)
                temp = self
                bin_times = reversed([int(i) for i in bin(abs(times))[2:]])
                for bit in bin_times:
                    if bit == 1:
                        result += temp
                    temp += temp
                return result
        else:
            raise TypeError("Can't multiply")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.curve == other.curve and self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self == other
    



    