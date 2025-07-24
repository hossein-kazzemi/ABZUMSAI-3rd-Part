
class BankAccount:
    bank_name = "First National Bank"

    # متد سازنده
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    # واریز پول
    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    # برداشت پول
    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount) and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount")

    # نمایش حساب
    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

    # تغییر نام بانک (متد کلاس)
    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to '{cls.bank_name}'")

    # بررسی معتبر بودن مبلغ (متد ایستا)
    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    # نمایش همه تراکنش‌ها
    def show_transactions(self) -> None:
        print(f"Transaction history for {self.account_holder}:")
        if not self.transactions:
            print("No transactions yet.")
        for t in self.transactions:
            print(t)

# کلاس فرزند: حساب پس‌انداز
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate  # نرخ بهره (به صورت کسری مثل 0.05)

    # افزودن سود به حساب
    def add_interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} added.")

    # نمایش با نرخ بهره
    def __str__(self) -> str:
        return f"Savings Account - Account Holder: {self.account_holder}, Balance: ${self.balance}, Interest Rate: {self.interest_rate*100}%"
    

savings_acc = SavingsAccount("Charlie", 1000, 0.05)
savings_acc.add_interest()
print(savings_acc)
