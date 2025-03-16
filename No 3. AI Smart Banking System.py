#Finance: AI-Based Smart Banking System

#Nama: Willy Syifa Luthfia
#NIM : 123140071

class BankAccount:
    #Kurs tetap untuk konversi mata uang
    exchange_rates = {
        ("USD", "EUR"): 0.9, ("EUR", "USD"): 1.1,
        ("USD", "IDR"): 15000, ("IDR", "USD"): 0.000067,
        ("EUR", "IDR"): 16500, ("IDR", "EUR"): 0.000061
    }

    def __init__(self, account_holder, balance, currency):
        #Inisialisasi akun dengan pemilik, saldo, dan mata uang
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency
    
    def __str__(self):
        #Mengembalikan informasi saldo akun dalam format string
        return f"{self.account_holder}'s Account: Balance = {self.currency} {self.format_balance(self.balance)}"
    
    def format_balance(self, amount):
        #Menghapus desimal jika angka bulat
        return int(amount) if amount.is_integer() else amount
    
    def convert_currency(self, amount, target_currency):
        #Mengonversi jumlah uang ke mata uang lain berdasarkan kurs tetap
        if self.currency == target_currency:
            return amount 
        rate = self.exchange_rates.get((self.currency, target_currency))
        if rate:
            converted = round(amount * rate, 2)  #Hasil konversi dibulatkan 2 desimal
            return self.format_balance(converted)  
        else:
            raise ValueError("Exchange rate not available")
    
    def __add__(self, other):
        #Menambahkan saldo dari akun lain dengan konversi mata uang jika perlu
        if isinstance(other, BankAccount):
            converted_amount = other.convert_currency(other.balance, self.currency)
            return BankAccount(self.account_holder, self.balance + converted_amount, self.currency)
        else:
            raise TypeError("Can only add another BankAccount object")
    
    def __sub__(self, amount):
        #Mengurangi saldo dan memberikan peringatan jika saldo tidak mencukupi
        if amount > self.balance:
            print("Insufficient balance for withdrawal!")  #Peringatan jika saldo kurang
        else:
            self.balance -= amount
            if self.balance < 100:
                print("Low Balance Warning!")  
        return self
    
    def apply_interest(self):
        #kalkulasi bunga: 2% untuk saldo >$5000, 1% untuk saldo dibawahnya
        interest_rate = 0.02 if self.balance >= 5000 else 0.01  
        self.balance += self.balance * interest_rate
        self.balance = round(self.balance, 2) 
        print(f"Applying interest... New Balance = ${self.format_balance(self.balance)}")

#Contoh Skenario
john = BankAccount("John", 5000, "USD")
emily = BankAccount("Emily", 1000, "EUR")

#Menampilkan saldo awal John sebelum bunga
print(f"{john.account_holder}'s Account: Initial Balance = ${john.format_balance(john.balance)}")
john.apply_interest()
print()

#Menampilkan saldo awal Emily sebelum konversi
print(f"{emily.account_holder}'s Account: Initial Balance = €{emily.format_balance(emily.balance)}")
converted_amount = emily.convert_currency(emily.balance, "USD")
print(f"Converted to USD: ${converted_amount}")
if converted_amount < 1200:
    print("Insufficient balance for withdrawal!") 
else:
    emily -= 1200  #Kurangi saldo setelah penarikan

#Menampilkan saldo akhir Emily setelah penarikan
print(f"{emily.account_holder}'s Account: Balance remains at €{emily.format_balance(emily.balance)}")
