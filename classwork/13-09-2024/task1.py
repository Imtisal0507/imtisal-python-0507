def hello(n):
    fac = 1
    for i in range(1,n+1):
        fac*=i
    return fac

print(hello())