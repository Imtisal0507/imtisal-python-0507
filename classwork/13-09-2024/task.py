def hello():
    n = int(input("Enter a number :"))

    fac = 1
    for i in range(1,n+1):
        fac*=i
    return fac


def add():
    n1 = int(input("Enter a number :"))
    n2 = int(input("Enter a number :"))
    return n1+n2


def cube():
    n = int(input("Enter a number :"))

    return n*n*n



print(hello())  
print(add())
print(cube())