balance = 1000

def deposit(amount):
    global balance
    balance += amount  
    print(f"New Balance is : {balance}")

def withdraw(amount):
    global balance
    balance -= amount  
    print(f"New Balance is : {balance}")

def main():
    d = float(input("Enter the amount to deposit: "))
    deposit(d)

    w = float(input("Enter the amount to withdraw: "))    
    withdraw(w)

main()

"""
create a menu
1.deposit
2. withdraw
3. Balance check
4. quit

ask user the choice

based on that deposit or withdraw 
"""
