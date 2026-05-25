# Account Identity and Status
#  Concepts Constructor, Object State, IBAN

from datetime import datetime   
import random
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self.generate_iban()
        self.transactions = []        
        self.creation_date = datetime.now()
        self.is_active =False

    def generate_iban(self):
        country_code = "CA"
        check_digits = str(random.randint(10, 99))
        bank_identifier = "BANK"
        account_number = str(random.randint(10000000, 99999999))
        return f"{country_code}{check_digits}{bank_identifier}{account_number}"

    def activate_account(self):
        self.is_active = True
        print(f"Account {self.account_number} is activated")

    def deactivate_account(self):
        self.is_active = False
        print(f"Account {self.account_number} is deactivated")



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

        print(f"Withdraw : {amount-fee}")
        print(f"New Balance is : {self.balance}")


    def account_info(self):
        print("\n========== ACCOUNT INFO ==========")
        print(f"Account Number      : {self.account_number}")
        print(f"Account Holder Name : {self.account_holder}")
        print(f"Balance             : ${self.balance:.2f}")
        print(f"Creation Date       : {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Account Active      : {self.is_active}")
        print("==================================")




account1 = BankAccount("Olu", 2000 )
account1.activate_account()
account1.deposit(500)
account1.withdraw(300)
account1.account_info()









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