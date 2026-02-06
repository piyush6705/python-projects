class bankAccount:
    def __init__(self,name,balance=0):
        self.name= name
        self.balance= balance
    
        
    def deposit(self,amount):
        if amount <=0:
            print("deposite amount must be positive")
            return 0
        else:
            self.balance += amount
            print(f"deposited  ${amount:.2f} successfully")

        

    def withdraw(self,amount):
        if amount <=0:
            print("withdraw amount must be positive")
            return 0
        elif amount > self.balance:
            print("insufficient funds")
            return 0
        else:
            self.balance -= amount
            print(f"withdrew ${amount:.2f} success")

    def check_balance(self):
        print(f"current balance: ${self.balance:.2f}")

name = input("Enter your name: ")
initial_balance = float(input("Enter initial balance: $"))
account = bankAccount(name, initial_balance)
is_running= True

while is_running:
    print("Welcome to the BAnk account system")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice= input("Please select an option (1-4): ")

    if choice == "1":
        account.check_balance()
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == "3":
        try:
            amount = float(input("Enter withdraw amount: $"))
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == "4":
        print(f"Thank you {account.name}. Goodbye!")
        is_running = False
    else:
        print("Invalid choice. Please select 1-4.")




