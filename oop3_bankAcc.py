
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        print('Account initial balance is:', self.balance)

    def debit(self, amount):
        self.balance -= amount
        print('Rs', amount, 'was debited.')
        print('Current balance is:', self.current_bal())

    def credit(self, amount):
        self.balance += amount
        print('Rs', amount, 'was credited.')
        print('Current balance is:', self.current_bal())

    def current_bal(self):
        return self.balance




account_a = Account(20000, 12345)
account_a.debit(3000)
account_a.credit(500)