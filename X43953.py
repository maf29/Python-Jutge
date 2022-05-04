N = int(input())
x = int(input())

cont = 0
successio = 0.0
while(N > 1 and cont < N):
     successio = successio + (x**cont/2**cont)
     cont += 1
print(successio)