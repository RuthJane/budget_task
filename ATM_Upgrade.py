
#initialising the system...
import random

database = {}

print("Welcome to RJ Bank.\n")

def init():
    
    ownAccount = int(input("Do you have account with us ? Press 1 for yes or 2 for no.\n"))
    if ownAccount == 1:
        login()
    elif ownAccount == 2:
        register()    
    else:
        print("Invalid entry.")
        init()

def login():
    print("login to your account.")
    account_num = generate_account_number()

    print(account_num)

    acctNumFromUser = int(input("What is your account number ? \n"))
    
    password = input("Enter your password.\n")
    for a, b in database.items():
        if account_num == acctNumFromUser:
            if b[3] == password:
                bank_operations(b)
                    
        print("Invalid account or password.")
        login()
               
    bank_operations()

def register():
    print("*****register*****")
    email = input("Enter your email address.\n")    
    first_name = input("Enter your first name.\n")
    last_name = input("Enter your last name.\n")
    password = input("Enter your password.\n")

    account_num = generate_account_number()

    database[account_num] = [first_name, last_name, email, password]
    print("Your account has been created.")
    print("===== ===== ===== =====")
    print("Your account number is {} ".format(account_num))
    print("Ensure you keep it safe.")
    print("===== ===== ===== =====")

    logout()

def bank_operations():
    user = database[account_num]
    print("operations function")
    print("Wellcome {} {} ".format(user[0], user[1]))
    selected_option = input("What would you like to do ? Press 1 to deposit, 2 to withdraw, 3 to logout, 4 to exit.")

    if selected_option == 1:
        deposit()
    elif selected_option == 2:
        withdrawal()
    elif selected_option == 3:
        login()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid Option Selected!")
        bank_operations()

def generate_account_number():
    print("generating account number...")
    return random.randrange(0000000000, 9999999999)

def withdrawal():
    print("withdrawal...")

def deposit():
    print("Deposit...")

def logout():
    login()

init()
#print(generate_account_number()) 