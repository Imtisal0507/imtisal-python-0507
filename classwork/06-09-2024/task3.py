"""""
a = int(input("Enter a number 1:"))
b = int(input("Enter a number 2:"))


temp = a
a = b
b = temp
"""

a,b = b,a
print("After swapping A :",a)
print("After swapping B :",b)
