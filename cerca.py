def igual(l):
    trobat=False
    i = 0
    while not len(l)-1 and not trobat:
        if l[i]%2==0:
            trobat=True
        else:
            i+=1
    return trobat

l=[1,2,3,4,5,6]
trobat = igual(l)
if trobat:
    print("Hi ha un element parell")
else:
    print("No hi ha un element parell")