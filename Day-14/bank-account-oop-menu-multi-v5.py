# Account Identity and Status
#  Concepts Constructor, Object State, IBAN
# If you wana generate IBAN from a python package https://schwifty.readthedocs.io/en/latest/examples.html#generation
# Add a bank account opening and menu to operate the bank
# How to have multiple accounts
# Show Statements

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
        opening_balance = user_deposit_amount if user_deposit_amount else 0
        account = cls(name, opening_balance)

        print(f"\nAccount created successfully!")
        print(f"{account.account_holder}'s account number is {account.account_number}")        
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
        print(f"{account_number} | {account.account_holder} | {account.balance:.2f} | Active: {account.is_active}")

    print(f"/n=======================================")
        


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
        print("10. Quit")
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

        elif choice == "10":
            print("\nThank you for using our bank.")
            break

        else:
            print("\nInvalid option. Please try again.")

main()









# account1 = BankAccount("Olu", 2000 )
# account1.activate_account()

# account1.deposit(500)
# account1.withdraw(300)
# account1.account_info()


# account2 = BankAccount("Clinton", 3000 )
# account2.deposit(1000)
# account2.account_info()

# account1.deposit(500)
# account1.account_info()









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