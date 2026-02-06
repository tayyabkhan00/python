class bank_account:
    def __init__(self):
        self.__balance=0
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("deposit:",amount)

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("withdraw:",amount)
        else:
            print("insufficient balance")
   
    def balance(self):
        return self.__balance

acc=bank_account()
acc.deposit(500)
acc.withdraw(200)
print(acc.balance())

# ---------------------------------------------------------
# ---------------------check-pin---------------------------
# ---------------------------------------------------------
class account:
    def __init__(self,pin):
        self.__pin=pin

    def check_pin(self,entered_pin):
        if self.__pin == entered_pin:
            print("your pin is correct")
        else:
            print("incorrect pin")

    def change_pin(self,old_pin,new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            print("pin change successfully")
        else:
            print("old pin is incorrect")

a=account(1234)
a.check_pin(1111)
a.check_pin(1234)
a.change_pin(1234,3456)
a.check_pin(3456)