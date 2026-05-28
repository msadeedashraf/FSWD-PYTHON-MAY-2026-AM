# Account Identity and Status
#  Concepts Constructor, Object State, IBAN
# If you wana generate IBAN from a python package https://schwifty.readthedocs.io/en/latest/examples.html#generation
# Add a bank account opening and menu to operate the bank
# How to have multiple accounts
# Show Statements
# Implementing Inheritance (Introduce Saving and Chequing Account)

from datetime import datetime   
import random
class BankAccount:
    global bank_name
    bank_name = "SADEED NATIONAL BANK"
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self.generate_iban()
        self.transactions = []        
        self.creation_date = datetime.now()
        self.Account_Type = "Chequing Account"
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


#  cls --- @classmethod
    @classmethod
    def open_account(cls):
        print(f"Welcome to {bank_name} \nLet's open an account")
        name = input("Enter your Account Title:")
        
        user_deposit_amount =  float(input("Enter the initial depost amount: "))

        print("\nSelect Account Type:")
        print("\n1. Saving Account")
        print("\n2. Chequing Account")

        account_type_choice = input("Enter the account type: ")
        
        if account_type_choice == "1":
            account = SavingsAccount(name, user_deposit_amount)
        
        elif account_type_choice == "2":
            account = ChequingAccount(name, user_deposit_amount)
            
        else:
            print(f"Invalid Choice. Creating a regular Bank Account.")
            account = BankAccount(name, user_deposit_amount)




        # opening_balance = user_deposit_amount if user_deposit_amount else 0
        # account = cls(name, opening_balance)

        print(f"\nAccount created successfully!")
        print(f"{account.account_holder}'s account number is {account.account_number}")        
        print(f"Account Type is : {account.Account_Type}")
        print(f"Account is currently deactivated\nPlease activate it.")


        return account



    def get_timstamp(self):
        current_time = datetime.now()

        timestamp = (
        current_time.strftime("%Y-%m-%d"), # Date part from the current date
        current_time.strftime("%I:%M:%S") # Time Part from the current date

            )
        return timestamp

    def deposit(self, amount):
        if self.is_active == False:
            return print(f"{self.account_holder} your account has to be active before depositing.\nContact the branch")

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


    def check_balance(self):
        print(f"Current balance for {self.account_holder} is {self.balance}")

    def account_info(self):
        print("\n========== ACCOUNT INFO ==========")
        print(f"Account Number      : {self.account_number}")
        print(f"Account Holder Name : {self.account_holder}")
        print(f"Balance             : ${self.balance:.2f}")
        print(f"Creation Date       : {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Account Active      : {self.is_active}")
        print(f"Account Type      : {self.Account_Type}")
        print("==================================")

        # =========================================================
    # FUNCTION: SHOW STATEMENT ON SCREEN
    # =========================================================

    def show_statement(self):

        if len(self.transactions) == 0:
            print("\nNo transactions to display.")
            return

        print("\n==============================================================")
        print("                    SADEED NATIONAL BANK")
        print("==============================================================")

        print(
            f"{'Date':<12}"
            f"{'Time':<12}"
            f"{'Description':<15}"
            f"{'Money In':>12}"
            f"{'Money Out':>12}"
            f"{'Balance':>12}"
        )

        print("-" * 75)

        for transaction in self.transactions:
            print(
                f"{transaction['date']:<12}"
                f"{transaction['time']:<12}"
                f"{transaction['type']:<15}"
                f"${transaction['money_in']:>11.2f}"
                f"${transaction['money_out']:>11.2f}"
                f"${transaction['balance']:>11.2f}"
            )

        print("-" * 75)
        print(f"{'Closing Balance':>63}: ${self.balance:.2f}")


def find_account(accounts):
    account_number = input("Enter the account number:")
    if account_number in accounts:
        return accounts[account_number]
    else:
        print("Account not found")
        return None
        
def list_all_accounts(accounts):
    if len(accounts) == 0:
        print(f"No account found")
        return
    print(f"/n=============ALL ACCOUNTS==============")

    for account_number, account in accounts.items():
        print(f"{account_number} | {account.account_holder} | {account.Account_Type} |{account.balance:.2f} | Active: {account.is_active}")

    print(f"/n=======================================")
        

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate=0.03):
        super().__init__(account_holder, balance)

        self.Account_Type = "Savings Account"
        self.interest_rate = interest_rate
    
    def add_interest(self):
        if not self.is_active:
            print("Account must be active before adding interest.")
            return
        interest = self.balance*self.interest_rate
        self.balance += interest

        timestamp = self.get_timstamp()

         # Dictionary
        transaction = {
        'type':'Interest',
        'date':timestamp[0],
        'time': timestamp[1],
        'money_in': interest,
        'money_out':0,
        'balance': self.balance
        }
        
        self.transactions.append(transaction)

        print(f"Added interest {interest} successfully." ) 
        print(f"New Balance for {self.account_holder} : {self.balance}")



class ChequingAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

        self.Account_Type = "Chequing Account"
        
    

# =========================================================
# MAIN PROGRAM
# =========================================================
def main():

    accounts = {}

    while True:
        print("\n=========== BANK ACCOUNT ==============")
        print("1. Open Account")
        print("2. Activate the Account")
        print("3. Deactivate the Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Show Balance")
        print("7. Show Account Info")        
        print("8. List All Accounts")
        print("9. Show Statement")
        print("10. Add Interest")

        print("11. Quit")
        print("=======================================")

        choice = input("Select an option: ")

        if choice == "1":
            account = BankAccount.open_account()
            accounts[account.account_number] = account


        elif choice == "2":
            account = find_account(accounts)
            if account:
                account.activate_account()
            

        elif choice == "3":
            account = find_account(accounts)
            if account:
                account.deactivate_account()
            

        elif choice == "4":
            account = find_account(accounts)
            if account:
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)

        elif choice == "5":
            account = find_account(accounts)
            if account:
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)

        elif choice == "6":
            account = find_account(accounts)
            if account:
                account.check_balance()
        
        elif choice == "7":
            account = find_account(accounts)
            if account:
                account.account_info()        

        elif choice == "8":
            list_all_accounts(accounts)
        
        elif choice == "9":
            account = find_account(accounts)
            if account:
                account.show_statement()

        elif choice =='10':
            account = find_account(accounts)

            if account: 
                if isinstance(account, SavingsAccount):
                    account.add_interest()
                else:
                    print("Interest can only be added to a Savings Account.")


        elif choice == "11":
            print("\nThank you for using our bank.")
            break

        else:
            print("\nInvalid option. Please try again.")

main()












