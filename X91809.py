n = int(input())
d = int(input())

aux = 0
contador = 0
while (n > 0 and 1 <= d <= 9) :
    aux = n % 10    #Mirar el modulo para comparar con d
    if(aux == d):
        contador = contador + 1 # o contador += 1
    n = n // 10     # ponemos // para coger la parte entera 
print("el numero ",d, "aparece :", contador, " veces")  # print(contador)
