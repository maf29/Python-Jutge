n=int(input())
s = 0
while(n > 0):      # n>0 : condición
    s = s + n%10    #accion_1
    n = n//10          #accion_2 y seguir_iterando
print(s)