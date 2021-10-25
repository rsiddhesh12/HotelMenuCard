plist=[]
class Hotel:
    def __init__(s,name='',email='',contact=0,password='',confirm_password='',p1=0,p2=0,tb=0):
        s.name=name
        s.email=email
        s.contact=contact
        s.password=password
        s.confirm_password=confirm_password
        s.p1=p1
        s.p2=p2
        s.tb=tb

    def __str__(s):
        return s.name+" "+s.email+" "+str(s.contact)+" "+s.password+" "+s.confirm_password+" "+str(s.p1)+" "+str(s.p2)

    
    def reg(s):
        try:
            s.name=input("Enter Your Name:")
            s.email=input("Enter Your Email:")
            s.contact=int(input("Enter You contact:"))
            s.password=input("Enter Your Password:")
            s.confirm_password=input("Confirm Password:")
        except Exception as e:
            print(e)
        else:
            if s.password==s.confirm_password:
                 h=Hotel(s.name,s.email,s.contact,s.password,s.confirm_password)
                 plist.append(h)
            else:
                print("Enter Your Information Again")
        
    def login(s):
        em=input("Enter Email :")
        passw=input("Enter Password :")
        for i in plist:
            if em==i.email and passw==i.password:
                print('Login Success \n',s.name,'\n',s.email)
                s.Order()
            else:
                print('Login Fail')
            
    def Veg(s):
        print ("-------------Veg Menu-------------")

        print ("1.  Veg Thali--------->Rs.600")

        print ("2.  Veg Briyani------->Rs.400")

        print ("3.  Paner Masala------>Rs.150")

        print ("4.  Veg Pulav--------->Rs.200")
        try:
            x=int(input("Enter Your Choice Please->"))

            n=int(input("Enter Quantity of your order:"))

            if(x==1):

                print ("you have opted Veg Thali")

                s.p1=600*n

            elif (x==2):

                print ("you have opted Veg Biryani")

                s.p1=400*n

            elif (x==3):

                print ("you have opted Paner Masala")

                s.p1=150*n

            elif (x==4):
                print ("you have opted veg Pulav")

                s.p1=200*n

            else:

                print ("please choose a Menu")
        except Exception as e:
            print(e)
        else:
            print ("Your Current Bill Amount  =",s.p1,"\n")
            for i in plist:
                i.p1+=s.p1
        finally:
            print("Place the oreder again")


    def Non_veg(s):
        print ("-------------Non-Veg Menu-------------")

        print ("1.  Non-Veg Thali--------->Rs.700")

        print ("2.  Mutton Briyani-------->Rs.450")

        print ("3.  Chicken Masala-------->Rs.250")

        print ("4.  Chicken 65------------>Rs.250")

        try:
            x=int(input("Enter Your Choice Please->"))

            n=int(input("Enter Quantity of your order:"))

            if(x==1):

                print ("you have opted Non-Veg Thali")

                s.p2=700*n

            elif (x==2):

                print ("you have opted Mutton Biryani")

                s.p2=450*n

            elif (x==3):

                print ("you have opted Chicken Masala")

                s.p2=250*n

            elif (x==4):
                print ("you have opted Chicken 65")

                s.p2=250*n

            else:


                print ("please choose a Menu")
        except Exception as e:
            print(e)
        else:
            print ("your Current bill Amount is =",s.p2,"\n")
            for i in plist:
                i.p2=i.p2+s.p2
        finally:
            print("place the order again")


    def Check_Detail(s):
        for i in plist:
            print(i)

    def Update(s):
        print("Enter email for Updating the user detail")
        em=input()
        for i in plist:
            if em==s.email:
                try:
                    i.name=input("Update Name:")
                    i.contact=int(input("Update Contact Number:"))
                    i.password=input("Update Password:")
                    i.confirm_password=input("Confirm Password:")
                except Exception as e:
                    print(e)
                else:
                    print("-------------SUCCESS-------------")
            else:
                print("Enter Valid Email Id")

    def delete(s):
        print("Enter Email Id for Delete Data:")
        em=input()
        for i in plist:
            if i.email==em:
                plist.clear()
                print("-------------SUCCESS-------------------")
            else:
                print("Enter Valid Email Id")
        

    def Bill(s):                
        for i in plist:
             i.tb=i.p1+i.p2
             print("Total Bill:",i.tb)
             print("Total Veg Bill:",i.p1)
             print("Total Non-veg Bill:",i.p2)

    def Order(s):
        choice=0
        while (choice!=7):
             print("Enter 1 for Veg Order")
             print("      2 for Non-Veg Order")
             print("      3 for TO check User Detail")
             print("      4 for to update User detail")
             print("      5 for to delete Account")
             print("      6 for to Check Total Bill")
             print("      7 for Exit")
             try:
                 choice=int(input())
             except Exception as e:
                 print(e)
             else:
                 if choice==1:
                     s.Veg()
                 elif choice==2:
                     s.Non_veg()
                 elif choice==3:
                     s.Check_Detail()
                 elif choice==4:
                     s.Update()
                 elif choice==5:
                     s.delete()
                 elif choice==6:
                     s.Bill()
           

   
def Operation():
    h=Hotel()
    choice=0
    while (choice!=3):
        print("Enter 1 Register")
        print("      2 Login")
        print("      3 exit")
        try:
            choice=int(input())
        except Exception as e:
            print(e)
        else:
            if choice==1:
                h.reg()
            elif choice==2:
                h.login()
            

            
Operation()

    
    
            
        
        

        
        
