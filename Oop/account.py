import time

class Account(object):
    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        self.transaction_history = []
        Account.count += 1

    def withdrawal(self, amount):
        if self.balance <= amount:
            print(f'残高が不足しています。残高:{self.balance}')
        else:
            self.balance -= amount
            print(f'{amount}万円引き出しました。')
            self.show_balance()
            self._add_transaction(-amount)

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount}万円入金しました。')
        self.show_balance()
        self._add_transaction(amount)

    def show_balance(self):
        print(f'>>>残高:{self.balance}万円、口座名:{self.name}、口座番号:{self.account_number}')

    def _add_transaction(self, amount):
        transaction = {
            'withdraw/deposit': amount,
            'new_balance': self.balance,
            'time': Account._get_time_str()
        }
        self.transaction_history.append(transaction)

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_list = []
            for k, v in transaction.items():
                transaction_list.append(f'{k}:{v}')
            print(', '.join(transaction_list))


    @staticmethod
    def _get_time_str():
        current_time = time.localtime()
        return '{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分'.format(current_time)


luffy = Account('Luffy', 1000)
zoro = Account('Zoro', 500)
nami = Account('Nami', 2000)

print('############')
luffy.withdrawal(90)
zoro.withdrawal(100)
nami.deposit(1000)
print(luffy.transaction_history)
luffy.show_transaction_history()


