#Feu un programa que, donat pel canal d’entrada un enter n més gran que zero, calculi el nombre de dígits que conté.
# 12340 ==> 5

n = int(input())
contador = 0

while (n > 0):
    n = n // 10
    contador += 1
    

print(contador)