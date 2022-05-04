N = int(input())

contador = 0
fibonacci = 0
anterior = 0
anterior_anterior = 0

if N > 1 :
    while(fibonacci < N):
        if(contador == 0):
            anterior = 1
            fibonacci = anterior
        elif(contador == 1):
            anterior_anterior = anterior
            anterior = 1
            fibonacci = anterior
        else:
            fibonacci = anterior + anterior_anterior
            anterior_anterior = anterior
            anterior = fibonacci
        
        if(fibonacci < N):
            print(fibonacci)
        contador += 1