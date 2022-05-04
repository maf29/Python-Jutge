#Donat un natural n, escriviu un programa que mostri la següent seqüència (de mida n):
#1, n, 2, n−1, 3, n−2, 4, n−3, … 

n = int(input())
contador = 1    #imprimir elementos 1 2 3 4 ...
b = 0   #contador de elementos que restarle a n 
x = 1   #contador de elementos imprimdos
while(x <= n):
    print(contador)
    x += 1
    if(x <= n):
        print(n - b)
    
    x += 1
    contador += 1
    b += 1
    