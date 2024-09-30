def mycall(n):
    fac = 1
    for i in range(1,n+1):
        fac*=i
    print(fac)

def pattern():
    for i in range(1,6):
        print("*"*i)


def pattern1():
    for i in range(1,6):
        print(" "*(6-i),"*"*i)

def pattern2():
    for i in range(1,6):
        print(" "*(6-i)," *"*i)        
    