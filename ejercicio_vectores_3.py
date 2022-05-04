#Muestra por pantalla todas las vocales de una cadena dada
# vocales : a e i o u
#cadena = "Buenas Maite, que tasl estas?"
cadena = "Hola!"
i = 0
while i < len(cadena):
    if(cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u"):
        print("en la posicion ", i, "de la cadena esta la vocal : ",cadena[i])
    i += 1