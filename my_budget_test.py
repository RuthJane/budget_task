list_item = {}
#category = []
class Budget():
    """A Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
    """
    category = ["food", "clothing", "entertainment"]
    
    def __init__(self, category):
        self.category = category
        self.mylist =  [] 
        self.balance = 100
        self.withdraw_amount = 50

    def check_funds(self, amount):
        if self.balance < amount:
            return False 
        else:
            return True 

    def deposit(self, amount, category):
        """Allows for depositing funds to categories.
        """
        print("\nYou deposited N"+ str(amount) + " for " + self.category)
        d = {
            "amount" : amount,
            "category" : self.category
        }
        self.mylist.append(d)
        list_item.update({
            "amount" : amount,
            "category" : self.category
        })
        self.balance = self.balance + amount 

    def withdraw(self, amount, category):

        if self.check_funds(amount) == True:
            print("You have some funds available.")
            self.withdraw_amount -= amount
            print("\nYou have withdrawn N" + str(amount) + " from " + self.category)
            print("\nYour balance is N{} ".format(self.withdraw_amount))
        else:
            print("\nInsufficient funds for {} ".format(self.category))
            return False 
            list_item.update({
            "amount" : self.balance,
            "category" : self.category})

    def compute_balance(self):
        """Computes category balance...
        """
        print("\nYour balance for {} is N".format(self.category), end="")
        return self.balance
        
    def transfer(self, amount, category):
        if self.check_funds(amount) == True: 
            self.balance -= amount 
            #list_item.update({
            #"amount" : self.balance,
            #"category" : self.category }) 
            self.ledger.append({"amount": -amount})
            print(self.mylist, end="")
            print(" transfer for {} ".format(self.category)) 
        else:
            self.withdraw(amount,f'Transfer from {self.category}')
            return False 

user_1 = Budget("food")
user_1.deposit(900, "food")
#user_1.check_funds(400)
#user_1.withdraw(10, "food")
print(user_1.compute_balance())
#user_1.transfer(0, "food")
#print(list_item)


