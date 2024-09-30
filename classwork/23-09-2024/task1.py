t = (1,2,3,4,5,6,7,"imtisal","imtisal",1.2555151,90)

print(type(t))

print(t.count("imtisal"))

print(t.index(4))

l =list(t)
print(l)
l.extend([100000,"python",2154851,252525])
print(l)


t1 = tuple(l)
print(t1)
