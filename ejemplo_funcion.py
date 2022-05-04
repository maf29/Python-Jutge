def operacion(z):
    b = z / ((z+1)*(z+2))
    return b

def suma(a):
    s = 0
    k = 1
    while k <= a:
        s = s + operacion(k)
        k = k+1
    return s

#programa princpial
n = int(input())
print(suma(n))