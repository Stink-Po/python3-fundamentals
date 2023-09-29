# what are objects

# entities created by python they have state(data) and they have methods(functionality)
# we call state and methods encapsulation
# they often represent real world things
# in python everything is object
# we can access to an object attributes with dot notation
# integer also have methods as you see below
a = 1
print(a.to_bytes())
print(a.__repr__())
b = a.__add__(2)
print(b.__repr__())


# mutability and immutability

# an object is mutable if its internal state can be change
# lists dictionary sets
# an object is immutable if its internal state cannot be changed
# integers floats booleans strings , ...

# custom object

class Account:
    def __init__(self, account_number, account_type, initial_balance):

        self.account_number = account_number  # state
        self.account_type = account_type  # state
        self.balance = initial_balance  # state

    # blow are objects functionality
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"deposited {amount},")
            print(f"new balance is : {self.balance}")
        else:
            print(f"{amount} is invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"withdraw : {amount}")
            print(f"New Balance is {self.balance}")
        else:
            if amount < 0:
                print(f"{amount} is invalid amount")

            else:
                print(f"insufficient found")
                print(f"Current balance is {self.balance}")


# new custom object

new_account = Account(account_number="123-456", account_type="saving", initial_balance=500.00)
print(f"account type is : {new_account.account_type}")
print(f"account numbers : {new_account.account_number}")
print(f"account balance: {new_account.balance}")
new_account.deposit(amount=1500.0)
print(f"account balance: {new_account.balance}")
new_account.withdraw(amount=100.0)
print(f"account balance: {new_account.balance}")


# we can get address of an object in memory with id(method)
id(a)