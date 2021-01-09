import asyncio
class Account:
    async def __init__(self,username,password,amount):
        self.username=username
        self.password=password
        self.amount=amount

    async def __repr__(self):
        return f"Account({self.username},{self.amount})"

class BankSystem :
    def __init__(self):
        self.accounts = []

   async def create_account ( self,username,password,amount )
        for i in self.accounts:
            if i.username == username:
                return "Username Already Exists"

        new = Account(username,password,amount)
        self.accounts.append(new)
        return "Account Created Succesfully"

    async def get_account(self,username,password):
        for i in self.accounts:
            if i.username == username and i.password == password:
                return i
        return False

    async def withdraw(self,username,password,amount):
        account  = self.get_account(username,password)
        if account == False:
            return "Invalid Username/Password"

        if amount > account.amount:
            return "Insufficient Balance"

        if amount > 0:
            account.amount -= amount
            return "WithDraw Successfully"
        else:
            return "Invalid Amount"
             
   async def deposit(self,username,password,amount):
        account = self.get_account(username,password)
        if account == False:
            return "Invalid Username/Password"
        if amount > 0:
            account.amount += amount
            return "Deposit Successfully"
        else:
            return "Invalid Amount"



BANK = BankSystem()

output = BANK.create_account (username = "sena"
                        password = '1234' ,amount=2000) :
print(output)
output = BANK.deposit (username = 'sena'
                      password = '1234', amount=1000) :
print(output)
output = BANK.withdraw (username = 'sena' ,
                       password = '1234' ,amount=1000) :
print(output)