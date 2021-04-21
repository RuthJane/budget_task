#register
#- username and password

#login
#username or email and password
def init():
    
    print("\nWelcome to RJ Bank.")

    welcome = int(input("Do you have an account with RJ Bank ? If yes press 1, if no press 2.\n"))
    #existing_user = False
    #while existing_user == True:

        if welcome == 1:
             
            user = input("Welcome back, enter your details to login.\n")
            login()
        
        elif welcome == 2:
            #existing_user = False
            user = input("Enter your fullname to proceed to register.\n").title()
            print("Welcome, {} ".format(new_user))
            register()

        else:
            print("Invalid entry. Try again.")    
        

        
def login():
    print("login function")

def register():
    print("register function")    

def bank_operations():
    print("operations function")   

def generate_account_number():
    print("generate accoount number funtion")     

init()    
