n = int(input())
while(n > 0):
    i = 1
    cont = 0
    while(i <= n):
        cont += i
        i += 1
    
    print(cont)
    n -= 1