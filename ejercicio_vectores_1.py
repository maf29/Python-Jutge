#Genera una lista de 10 numeros enteras entrados por teclado
l = []
i = 0
while i < 10:
        element = int(input("introduce elemento de ls lista: "))
        l.append(element)
        i += 1
print("lista tiene: ", len(l), " elementos : ",l ) 
