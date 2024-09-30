d ={1:"Hello",2:"Welcome",3:"India"}
print(d.get(1))
print(d.items())
print(d.keys())
d.popitem()
print(d)


d.pop(2)
print(d)


d.update({6:"Tiger",7:"Lion",8:"Bear"})
print(d)


t = (1,2,3)
d1 ={}
print(d1.fromkeys(t))

