#Donat un natural n > 0, dissenyeu un programa que en mostri tots els seus divisors.
n = int(input())
div = 1

while(n > 0 and div <= n):
    if(n % div == 0):   #al dividir n entre d su resto sea = 0 es decir que es divisible
        print(div)
    div += 1