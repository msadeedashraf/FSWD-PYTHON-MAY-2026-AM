from datetime import datetime   
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []        


    def get_timstamp(self):
        current_time = datetime.now()

        timestamp = (
        current_time.strftime("%Y-%m-%d"), # Date part from the current date
        current_time.strftime("%I:%M:%S") # Time Part from the current date

            )
        return timestamp

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
            return
        
        self.balance +=amount
        
        timestamp = self.get_timstamp()

         # Dictionary
        transaction = {
        'type':'Deposit',
        'date':timestamp[0],
        'time': timestamp[1],
        'money_in': amount,
        'money_out':0,
        'balance': self.balance
        }
        
        self.transactions.append(transaction)

        print(f"Dposited : {amount} successfully." ) 
        print(f"New Balance for {self.account_holder} : {self.balance}")


    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient funds")
            return


        fee = 2
        amount  += fee

        self.balance -= amount  

        timestamp = self.get_timstamp()

            
        # Dictionary
        transaction = {
            'type':'Deposit',
            'date':timestamp[0],
            'time': timestamp[1],
            'money_in': 0,
            'money_out':amount,
            'balance': self.balance
        }
        


        self.transactions.append(transaction)

        print(f"Withdraw : {amount}")
        print(f"New Balance is : {self.balance}")



oluAccount = BankAccount("Olu", 2000)
oluAccount.deposit(100)


oluAccount = BankAccount("Andrea", 1000)
oluAccount.deposit(300)




'''
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(self.balance)

clintonAccount = BankAccount("Clinton", 1000)
andreaAccount = BankAccount("Andrea", 2000)
shannonAccount = BankAccount("Shannon", 3000)
dalalAccount = BankAccount("Dalal", 4000)
oluAccount = BankAccount("Olu", 5000)

clintonAccount.deposit(200)
clintonAccount.show_balance()

andreaAccount.deposit(500)
andreaAccount.show_balance()

'''