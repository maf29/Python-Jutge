pmin=float(input())
pmax=float(input())
seq=float(input())
c=0
trobat=True
while seq!=0 and trobat:
    print(seq<pmin)
    if seq<pmin or seq>pmax:
        trobat=False
        print("NUMERO MAL")
    else:
        c+=1
        seq=float(input())
if trobat:
    print("Si")
else:
    print("No ", c)