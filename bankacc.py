class BankAccount:
    def __init__(self, name, balance, secret):
        self.name = name
        self._balance = balance
        self._secret = secret

    def verify(self, secret):
        return self._secret == secret
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Balance is not enough.")
            return
        self._balance -= amount
        print("withdraw succesfully!")
        print(f"Your remaining balance is {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print("Deposit Successfully!")
        print(f"Your remaining balance is {self._balance}")

    def check_balance(self):
        print(f"Hello {self.name}. Your remaining balance is {self._balance}")

class SavingAccount(BankAccount):
    def calculate_interest(self):
        self._balance += 10
        print("Interested Received: 10$")
        print(f"Your remaining balance is {self._balance}")

class StudentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 100:
            print("You can't withdraw more than 100$")
            return
        super().withdraw(amount)

class BusinessAccount(BankAccount):
    def take_loan(self, amount):
        print("You took load successfully!")
        self._balance += amount
        print(f"Thank You! Your balance is {self._balance}")

accounts = {}
current_user = None

while True:
    print('''=== ATM SYSTEM ===
    choose Menu
====================
1. CREATE ACCOUNT
2. LOGIN
3. CHECK BALANCE
4. WITHDRAW
5. DEPOSIT
6. TRANSFER
7. LOGOUT
====================
''')
    choice = input("Select Menu: ")
    if choice == "1":
        name = input("Input account name: ")
        if name in accounts:
            print("Account name is existed.")
            continue

        balance = float(input("Input initial balance: "))
        secret = input("Input your secret: ")
         
        acc = BankAccount(name, balance, secret)
        accounts[name] = acc

        print("Bank account is created successfully!")

    #login
    elif choice == "2":
        name = input("Input account name: ")
        secret = input("Input secret PIN: ")

        if name in accounts and accounts[name].verify(secret):
            print("")
            print(f"Login success! Welcome {name}! ")
            print("")
            current_user = accounts[name]
        print("Invalid account name or secret")

    elif choice == "3":
        if current_user is None:
            print("Please login first")
            continue
        current_user.check_balance()

    elif choice == "4":
        if current_user is None:
            print("Please login first")
            continue
        amount = float(input("Input amount: "))
        current_user.withdraw(amount)

    elif choice == "5":
        if current_user is None:
            print("Please login first")
            continue
        print("=== DEPOSIT ===")
        amount = float(input("Input deposit amount: "))
        current_user.deposit(amount)
        
    elif choice == "6":
        if current_user is None:
            print("Please login first")
            continue
        receiver = input("Input receiver account name: ")
        if receiver not in accounts:
            print("Receiver account not found.")
            continue
        amount = float(input("Input transfer amount: "))
        if amount > current_user._balance:
            print("Your balance is not enough.")
            continue
        current_user._balance -= amount
        accounts[receiver]._balance += amount
        print("Transfer successfully!!")
    
    elif choice == "7":
        current_user = None
        print("Logout success!!")