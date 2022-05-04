filas = int(input("cuantas filas tendra la matriz :"))
columnas = int(input("cuantas columnas tendra la matriz :"))

M = []
#leer
for i in range(filas) :
    M.append([])
    for j in range(columnas) :
        elemento = int(input("Entra el valor : "))
        M[i].append(elemento)

#imprimir
for i in range(len(M)) :
    for j in range(len(M[0])) :
        print("Elemento de la fila[",i,"] columna [",j,"] :", M[i][j])