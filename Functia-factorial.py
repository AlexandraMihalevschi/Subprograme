m = int(input("Valoarea lui m = "))
n = int(input("Valoarea lui n = "))

def factorial(x):
    p = 1
    if x>0:
        for i in range(1, x+1):
            p = p*i
    else: print("Valoarea ", x, " nu poate avea factorial")
    return p

c = factorial(n)/(factorial(m)*factorial(n-m))
print("C =", int(c))