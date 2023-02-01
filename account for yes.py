print ("welcome to isg")
Acc = input ("do you have an account ")
if Acc == "yes":
    print ("please Login:\n ")
    User_name= input("UserName: ")
    pass_ = input ("Password: ")
    count = 2
    pass_ = input (" Enter password ")
    
    while count > 0:
        if pass_ == "1234":
            print("welcome")
        else:
            retry = input(" Retry password")
            count -=1
            print(" Login Failed ")
        break
    print("welcom to your child's profile, what would you like to see ")
    print ("\n1.Behavious , \n2.Accademics, \n3.sport, \n4.Homework")
    
    select = input ("select: ")
    if select == "1" :
                    print("he is very active in class but")
                    print("\n - sipho is noisy in class, \n -he eat during lessons,")
    elif select =="2" :
         print("sipho's profile")
         print("\n-Maths 100%, \n-LO 99%")
    elif select =="3" :
         print("Tuesday:baseball")
         print("mondy: soccer")
         
    elif select =="4" :
         print("sipho's profile")
         print("\nMaths solve for x,\nscience:human body parts")          
    
                   
                           

    
elif Acc == "no":
    print("please resgiter")
    first_name = input ("Name: ")
    surname = input("Surname: ")
    email = input(" Email: ")
    pass_word = input ("password: ")
    print ("confirm password ")
    pass_word2 = input("confrm password: ")
    if pass_word == pass_word2:
        print("account confirmed")
    else:
        print("Password does not match")
        quit()
        print("welcom to your child's profile, what would you like to see ")
        print ("\n1.Behavious , \n2.Accademics, \n3.sport, \n4.Homework")
        

else:
        quit()
                
            
       

