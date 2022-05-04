#Donat dos naturals x, y tals que 2 < x ≤ y, escriviu un programa que calculi la suma dels nombres de Fibonacci 
# que es trobin dins d’aquest interval (x,y). Per exemple, si l’interval és (2,6), els nombres de Fibonacci que pertanyen a aquest interval
#  son 2, 3 i 5 per tant el resultat serà:
#10 = 2 + 3 + 5 
# La definició de la sèrie dels nombres de Fibonacci és:
#               F0 = 1
#               F1 = 1
#               Fn = Fn−1 + Fn−2

x = int(input())
y = int(input())
anterior_anterior = 1
anterior = 1
contador = 0
if(2 <= x <= y):
    actual = 2
    while(actual <= y):
        aux = anterior
        anterior = anterior_anterior + anterior
        anterior_anterior = aux
        
        if(actual >= x and anterior <= y):    #si estamos en el intervalo x,y y el anterior sea menor que y
            contador += anterior
       
        actual += 1

print(contador)

