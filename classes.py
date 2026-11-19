class Client:
    def __init__(self, name, last_name, pin):
        self.name = name
        self.last_name = last_name
        self.accounts = []
        self.pin = pin
    def __str__(self):
        return f"{self.name} {self.last_name}"

    def get_accounts(self):
        return ", ".join(str(account) for account in self.accounts)

    

class BankAccount:
    bank_name = "UENO Bank"
    def __init__(self, account_number, client, currency="EUR"):
        self.account_number = account_number
        self.balance = 0
        self.currency = currency
        self.client = client
        self.client.accounts.append(self)

    def __str__(self):
        return f"Nº: {self.account_number}, Saldo: {self.get_balance()}, Propietario: {self.client}"

    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"Ingresaste {amount} {self.currency} en la cuenta {self.account_number}. Saldo actual: {self.balance} {self.currency}"

    def withdraw(self,amount):
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True

    def get_balance(self):
        return f"{round(self.balance, 2):.2f} {self.currency}"

    def get_bank_name(self):
        return self.bank_name