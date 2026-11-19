class Client:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename
        def __str__(self):
            return f"{self.name} {self.surename}"

class BankAccount:
    bank_name = "Dios supremo legitimo Uriel Cuartas"
    def __init__(self, account_number, client_name, currency="EUR",):
        self.account_number = account_number
        #guardamos el dinero en integer
        self.balance = 0
        self.currency = currency
        self.client = client_name

    def deposit(self,amount):
        self.balance += amount


    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True

    def get_balance(self):
        return f"{self.balance: .2f} {self.currency}"

cliente1 = Client("Juan", "Perez")
    

cuenta1 = BankAccount("1111111")

print(cuenta1. account_number)
print(f"Tiene: {cuenta1.balance} {cuenta1.currency}")

cuenta1.deposit(12.99)
print (cuenta1.account_number, f"Tiene: {cuenta1.balance} {cuenta1.currency}, y el propietario es {cuenta1.cliente1.name}")
print(cuenta1.withdraw(1.9), f"Tiene {cuenta1.balance} {cuenta1.currency} {cuenta1.cliente1.name}")
