trobat=False
ant=int(input())
actual=int(input())
while actual!=0 and not trobat: 
    if ant>actual:
        trobat=True
    else:
        ant=actual
        actual=int(input())
if trobat: 
    print("No està ordenar de manera creixent")
else: 
    print("Està ordenar de manera creixent")