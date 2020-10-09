a,b,n=1,2,0
while b<4000000:
    a,b,n=b,a+b,n+((b+1)%2)*b
print(n)