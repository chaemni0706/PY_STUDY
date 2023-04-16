def open_account():
    print("new accont is created")

open_account()

def deposit(balance, money):
    print("ok. money is {0}".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance>=money:
        print("ok. money is {0}".format(balance-money))
        return balance-money
    else:
        print("no, money is {0}".format(balance))

def withdraw_night(balance, money):
    commission=100
    return commission, balance-money-commission

balance=0
balance=deposit(balance, 1000)
commission, balance=withdraw_night(balance, 500)
print("commission is {0}, money is {1}".format(commission, balance))
