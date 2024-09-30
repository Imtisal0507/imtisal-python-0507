from task1 import *


while True:
    menu = """
    press 1 for factorial
    press 2 for pattern
    press 3 for pattern1
    press 4 for pattern2
    press 5 for exit
    """

    print(menu)
    choice = int(input("Enter a choice :"))


    if choice==1:
        n = int(input("Enter a number :"))
        mycall(n)
    elif choice==2:
        pattern()

    elif choice==3:
        pattern1()

    elif choice==4:
        pattern2()

    elif choice==5:
        print("Thank you ")
        break
    else:
        print("Invalid choice!!!!!!!!!!!!!!!!!!!!!!")
        break