
class BankAccount:
    def __init__(self, name, balance, secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def withdraw(self):
        print("=== Withdrawing Balance ===")
        secret = input("Input your secret number:  ")

        if secret == self.__secret:
            amount = float(input("Input your amount:  "))
            remain = self.__balance - amount

            if remain < 0:
                print("your balance is not enough to withdraw.")
            else:
                self.__balance = remain
                print("...Withdrawal Successfully...")
                print(f"Your remaining balance is: {self.__balance}")
        else:
            print("Sorry, we dont't know you")

    def Check_Balance(self):
        print("=== Checking Balance ===")
        secret = input("Input your secret number: ")

        if secret == self.__secret:
            print(f"Hello User: {self.name}")
            print(f"Your remaining balance is {self.__balance}")
        else:
            print("Sorry, we don't know you.")

    def deposit(self):
        print("User is depositing")

    # saving account inherits from bank account
class SavingAccount(BankAccount):
    def Calculate_Interest(self):
        print(f"Your Balance now is {self._BankAccount__balance}")

    # student bank account inherits from bank account
class StudentBankAccount(BankAccount):
    def withdraw(self):
        print("==== Student Withdraw ====")
        secret = input("Input your secret number: ")

        if secret == self._BankAccount__secret:
            amount = float(input("Input your amount: "))

            if amount > 500:
                print("You cannot withdraw more than 500$")
            else:
                self._BankAccount__balance -= amount
                print(f"Your balance now is {self._BankAccount__balance}")
        else:
            print("We dont know you.")

    # premium saving account inherits from saving bank account
class PremiumSaving(SavingAccount):
    def deposit(self):
        print("==== Premium Deposit ====")
        amount = float(input("Input deposit amount: "))

        bonus = amount * 0.02
        self._BankAccount__balance += amount + bonus

        print(f"Bonus: {bonus}")
        print(f"Your balance now is {self._BankAccount__balance}")

    # business account inherits from bank account
class BusinessAccount(BankAccount):
    def take_loan(self):
        loan = float(input("Input loan amount: "))
        self._BankAccount__balance += loan
        print(f"Loan added. Balance now is {self._BankAccount__balance}")

    # Create Saving Account
atar = SavingAccount(name="atar", balance=20000, secret="2903")
atar.withdraw()
atar.Check_Balance()
atar.Calculate_Interest()

    # Create Student Bank Account
student = StudentBankAccount(name="atar", balance=1000, secret="2903")
student.withdraw()          
student.Check_Balance()

    # Create Premium Saving Account
premium = PremiumSaving(name="atar", balance=5000, secret="2903")
premium.deposit()          
premium.Calculate_Interest()

    # Create Business Account
business = BusinessAccount(name="atar", balance=10000, secret="2903")
business.take_loan()        
business.Check_Balance()
