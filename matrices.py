A = [[1,4,5,12],
    [-5,8,9,0],
    [-6,7,11,19]]

column=[]
for row in A:
    column.append(row[2])
print("columna 3 : ", column)


print ("columnas: ",len(A[0]))
print ("filas: ",len(A))

#añadir ultima columna
for i in range(len(A)):   #recorrer filas para introducir elemento por columna 
    elemen_fila = int(input("introduce elemento de la nueva columna :"))
    A[i].append(elemen_fila)
print(A)

#añadir ultima fila
A.append([])
for i in range(len(A[0])):   #recorrer columnas para introducir elemento por fila 
    elemen_fila = int(input("introduce elemento de la nueva fila :"))
    A[len(A)-1].append(elemen_fila)
print(A)


print ("columnas: ",len(A[0]))
print ("filas: ",len(A))

