class Hotel:
    def __init__(s,name,email,contact,password,confirm_password,p1,p2,tb):
        s.name=name
        s.email=email
        s.contact=contact
        s.password=password
        s.confirm_password=confirm_password
        s.p1=p1
        s.p2=p2
        s.tb=tb

    def __str__(s):
        return s.name+" "+s.email+" "+str(s.contact)+" "+s.password+" "+s.confirm_password+" "+str(s.p1)+" "+str(s.p2)+" "+str(s.tb)
    

def Operation():
        plist=[]
        choice=0
        while (choice!=3):
            print("Enter 1 Register")
            print("      2 Login")
            print("      3 exit")
            choice=int(input())

            if choice==1:
                print('------------Enter registration detail----')
                name=input("Enter Your Name:")
                email=input("Enter Your Email:")
                contact=int(input("Enter You contact:"))
                password=input("Enter Your Password:")
                confirm_password=input("Confirm Password:")
                if password==confirm_password:
                    p1=0
                    p2=0
                    tb=0
                    h=Hotel(name,email,contact,password,confirm_password,p1,p2,tb)
                    plist.append(h)
                else:
                    print("Sorry Password and Confirm password is not same")
            elif choice==2:
                em=input("Enter Email :")
                pas=input("Enter Password :")
                for i in plist:
                    if i.email==em and i.password==pas:
                        print('LOGIN SUCCESS')
                        print('Name: ',i.name)
                        print('Email ID: ',i.email)
                        while(choice!=7):
                            print("Enter 1 for Veg Order")
                            print("      2 for Non-Veg Order")
                            print("      3 for TO check User Detail")
                            print("      4 for to update User detail")
                            print("      5 for to delete Account")
                            print("      6 for to Check Total Bill")
                            print("      7 for Exit")
                            choice=int(input())  

                            if choice==1:
                                print ("-------------Veg Menu-------------")

                                print ("1.  Veg Thali--------->Rs.600")

                                print ("2.  Veg Briyani------->Rs.400")

                                print ("3.  Paner Masala------>Rs.150")

                                print ("4.  Veg Pulav--------->Rs.200")

                                x=int(input("Enter Your Choice Please->"))

                                n=int(input("Enter Quantity of your order:"))

                                if(x==1):

                                    print ("you have opted Veg Thali")

                                    p1=600*n

                                elif (x==2):

                                    print ("you have opted Veg Biryani")

                                    p1=400*n

                                elif (x==3):

                                    print ("you have opted Paner Masala")

                                    p1=150*n

                                elif (x==4):
                                    print ("you have opted veg Pulav")

                                    p1=200*n

                                else:

                                    print ("please choose a Menu")

                                print ("Your Current Bill Amount  =",p1,"\n")
                                for i in plist:
                                    i.p1+=p1
                                
    
                            elif choice==2:
                                print ("-------------Non-Veg Menu-------------")

                                print ("1.  Non-Veg Thali--------->Rs.700")

                                print ("2.  Mutton Briyani-------->Rs.450")

                                print ("3.  Chicken Masala-------->Rs.250")

                                print ("4.  Chicken 65------------>Rs.250")

                                x=int(input("Enter Your Choice Please->"))

                                n=int(input("Enter Quantity of your order:"))

                                if(x==1):

                                    print ("you have opted Non-Veg Thali")

                                    p2=700*n

                                elif (x==2):

                                    print ("you have opted Mutton Biryani")

                                    p2=450*n

                                elif (x==3):

                                    print ("you have opted Chicken Masala")

                                    p2=250*n

                                elif (x==4):
                                    print ("you have opted Chicken 65")

                                    p2=250*n

                                else:

                                    print ("please choose a Menu")
                                
    
                                print ("your Current bill Amount is =",p2,"\n")
                                for i in plist:
                                    i.p2=i.p2+p2

                                
                            elif choice==3:
                                 for i in plist:
                                     print(i)
                            elif choice==4:
                                 print("Enter email for Updating the user detail")
                                 em=input()
                                 for i in plist:
                                         if i.email==em:
                                            i.name=input("Update Name:")
                                            i.contact=int(input("Update Contact Number:"))
                                            i.password=input("Update Password:")
                                            i.confirm_password=input("Confirm Password:")
                                            print("-------------SUCCESS-------------")
                                                
                            elif choice==5:
                                print("Enter Email Id for Delete Data:")
                                em=input()
                                for i in plist:
                                    if i.email==em:
                                        plist.remove(i)
                                        print("-------------SUCCESS-------------------")

                            elif choice==6:
                                for i in plist:
                                     i.tb=i.p1+i.p2
                                     print("Total Bill:",i.tb)
                                     print("Total Veg Bill:",i.p1)
                                     print("Total Non-veg Bill:",i.p2)                                       
                                                                
                else:
                    print('Login Again')
                       
                        

                        
Operation()

            
           
