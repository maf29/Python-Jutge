n = int(input())

contador = 0

while (n > 0):
    contador += n % 10    #mirar el resto
    n = n // 10
print(contador)