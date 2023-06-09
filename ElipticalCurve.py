
INF_POINT = None
class EllipticCurve:
    def __init__(self ,p ,a ,b):
        self.p = p
        self.a = a
        self.b = b

    def reduce_modp(self ,x):
        return x % self.p

    def equal_modp(self ,x ,y):
        return self.reduce_modp(x - y) == 0

    def inverse_modp(self ,x):
        if self.reduce_modp(x) == 0:
            return None
        return pow(x, p- 2, p)

    def addition(self, P1, P2):
        if P1 == INF_POINT:
            return P2
        if P2 == INF_POINT:
            return P1
        (x1, y1) = P1
        (x2, y2) = P2
        if self.equal_modp(x1, x2) and self.equal_modp(y1, -y2):
            return INF_POINT
        if self.equal_modp(x1, x2) and self.equal_modp(y1, y2):
            u = self.reduce_modp((3 * x1 * x1 + self.a) * self.inverse_modp(2 * y1))
        else:
            u = self.reduce_modp((y1 - y2) * self.inverse_modp(x1 - x2))
        v = self.reduce_modp(y1 - u * x1)
        x3 = self.reduce_modp(u * u - x1 - x2)
        y3 = self.reduce_modp(-u * x3 - v)
        return (x3, y3)

    def multiple(self, k, P):
        Q = INF_POINT
        if k == 0:
            return Q
        while k != 0:
            if k & 1 == 1:
                Q = self.addition(Q, P)
            P = self.addition(P, P)
            k >>= 1
        return Q

    def is_point_on_curve(self, x, y):
        return self.equal_modp(y * y, x * x * x + self.a * x + self.b)


# mainline
# Builds the Elliptic Curve Parameters and Generating Point
choice = int(input("Do you want to build small[1] or big[2]?"))
akey = int(input("What is the private key for Alice? "))
bkey = int(input("what is the private key for Bob? "))

if choice == 2:
    p = 26959946667150639794667015087019630673557916260026308143510066298881
    a = -3
    b = 18958286285566608000408668544493926415504680968679321075787234672564
    Gx = 19277929113566293071110308034699488026831934219452440156649784352033
    Gy = 19926808758034470970197974370888749184205991990603949537637343198772
else:
    p = 19
    a = 2
    b = 7
    Gx = 11
    Gy = 7
PXXX = EllipticCurve(p, a, b)
G = (Gx, Gy)

# Prints Elliptic Curve and Generating Point
print("p = ", p)
print("a = ", a)
print("b = ", b)
print("Gx = ", Gx)
print("Gy = ", Gy)

# Publish Public Key
multiple = akey * bkey
Q = PXXX.multiple(multiple, G)
print("Keys are", PXXX.is_point_on_curve(Q[0], Q[1]), "verified")
print("The public key is ...")
print("x =", Q[0])
print("y =", Q[1])