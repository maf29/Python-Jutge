#Donat un natural N > 1 pel canal d’entrada, feu un programa que calculi els nombres primers més grans o iguals que N en ordre creixent. 
#Recordeu que un nombre és primer si els seus divisors són únicament 1 i n.

N = int(input())
primo = 2
while(N > 1 and primo < N):
    bool = True
    
    div = 2
    while(div <= primo):
        if(primo % div == 0 and div != primo):  #si es divisible entre un numero que no sea 1 y el propio numero, es FALSE
            bool = False    
        div += 1
    if (bool != False):
        print(primo)
    primo += 1