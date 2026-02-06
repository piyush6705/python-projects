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

    def veryfy_pin(self, entered_pin):
        return self.pin == entered_pin

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
pin = int(input("Set a 4 ddigit PIN: "))
account = bankAccount(name, initial_balance,pin)
is_running= True

attempts= 3

while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))
    if account.verify_pin(entered_pin):
        print("pin verified")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN ,Attempts left: {attempts}")

if attempts == 0:
    print("Too many wrong attempts. Account locked for some securityy reasason")
    exit()




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
            print("INVALID AMOUNT. Please enter a number.")
    elif choice == "3":
        try:
            amount = float(input("Enter withdraw amount: $"))
            account.withdraw(amount)
        except ValueError:
            print("INVALID AMOUNT. Please enter a number.")
    elif choice == "4":
        print(f"Thank you {account.name}. Goodbye!")
        is_running = False
    else:
        print("INVALID CHOICE. Please select 1-4.")




