print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!welcome to a website!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


while True:
    print("Choose a number for booking")
    print("press 1 for PVR")
    print("press 2 for rajhans")
    print("press 3 for INOX")
    print("press 4 for exit")

    choice=int(input("Enter a choice :"))
    if(choice==1):
        print("450 for a recliner")
        print("350 for platinum")
        print("250 for gold")
        n1=int(input("Enter your seat :"))
        if n1==1:
            print("You choose recliner")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*450)+(Ticket*450*0.009)
            print("Your total is",count)
        elif n1==2:
            print("You choose platinum")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*350)+(Ticket*350*0.009)
            print("Your total is",count)
        elif n1==2:
            print("You choose gold")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*250)+(Ticket*250*0.009)
            print("Your total is",count)
        break

    elif(choice==2):
        print("400 for a recliner")
        print("300 for platinum")
        print("200 for gold")

    choice=int(input("Enter a choice :"))
    if(choice==1):
        print("400 for a recliner")
        print("300 for platinum")
        print("200 for gold")
        n1=int(input("Enter your seat :"))
        if n1==1:
            print("You choose recliner")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*400)+(Ticket*400*0.009)
            print("Your total is",count)
        elif n1==2:
            print("You choose platinum")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*300)+(Ticket*300*0.009)
            print("Your total is",count)
        elif n1==2:
            print("You choose gold")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*200)+(Ticket*200*0.009)
            print("Your total is",count)
        break 

    elif(choice==3): 
        print("550 for a recliner")
        print("400 for platinum")
        print("300 for gold")
    choice=int(input("Enter a choice :"))
    if(choice==1):
        print("550 for a recliner")
        print("400 for platinum")
        print("300 for gold")
        n1=int(input("Enter your seat :"))
        if n1==1:
            print("You choose recliner")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*550)+(Ticket*550*0.009)
            print("Your total is",count)
        elif n1==2:
            print("You choose platinum")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*400)+(Ticket*400*0.009)
            print("Your total is",count)
        elif n1==2:
            print("You choose gold")
            print("How many ticket you want")
            Ticket = int(input("Enter number of ticket:"))
            count=(Ticket*300)+(Ticket*300*0.009)
            print("Your total is",count)
        break


    else: 
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Thank you to visit our website!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break



    










