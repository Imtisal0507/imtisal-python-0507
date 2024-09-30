import random
otp = random.randint(1001,9999)
d = {}
while True:
    menue="""
    press 1 for signup 
    press 2 for loin
    press 3 for Forgot oassword
    press 4 for Exit
"""

    print(menue)

    choice = int(input("Enter choice :"))


    if choice==1:
        print("*"*50,"Welcome to signup page","*"*50)
        name = input("Enter name :")
        email = input("Enter e mail:")
        mobile = int(input("Enter mobile number :"))
        password = int(input("Enter password :"))
        Cpasword = int(input("Enter confirm password :"))


        if password==Cpasword:
            d['name']=name
            d['email']=email
            d['mobile']=mobile
            d['password']=password
            print("Signup Sucessfully!!!")
        else:
            print("Password & confirm password does not match!!!")
    elif choice==2:
        print("*"*50,"Welcome to login page","*"*50)
        email = input("Enter Email :")
        password = int(input("Enter Password :"))


        if d['email']==email and d['password']==password:
            print("Login sucessfully!!!")
        else:
            print("Invalid password!!!")

    elif choice==3:
        mobile = int(input("Enter mobile number :"))


        if d['mobile']==mobile:
            print("*"*50,"Your OTP is :",otp,"*"*50)

            uotp = int(input("Enter OTP:"))

            if uotp==otp:
                password = int(input("Enter New password :"))


                d['password']=password

            else:
                print("Invalid OTP!!!") 


    elif choice==4:
        print("Thank you!!!")
        break
    else:
        print("Invalid choice!!!") 
