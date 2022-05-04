from math import sqrt
n=int(input())
x=float(input())
r=0
k=0
s=0
while k<=n:
    s=s+(x+k**3)/((k+1)**2*(k+2)**2)
    k+=1
r=sqrt(s)
print(r)