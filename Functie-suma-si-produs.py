a = int(input("Numaratorul 1 fractie: "))
b = int(input("Numitorul 1 fractie: "))
c = int(input("Numaratorul 2 fractie: "))
d = int(input("Numitorul 2 fractie: "))

def adunare(x, y, z, p):
    if z*p!=0:
        s = ((x*p)+(y*z))/(z*p)
        return s
    else: print("Nu exista")
    

def inmultire(x, y, z, p):
    if y*p!=0:
        p = (x*z)/(y*p)
        return p
    else: print("Nu exista")
    

print("Suma este ", round(adunare(a, b, c, d), 2), " iar produsul este ", round(inmultire(a, b, c, d), 2))