#Definind functia-putere, sa se calculeze valoarea expresiei S
def putere(x, y):
    return x**y

s = 1 + putere(0.5, 2) + putere(0.5, 4) + putere(0.5, 6) + putere(0.5, 8)
print("S =", s)