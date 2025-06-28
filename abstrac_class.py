"""
Abstract Class (ABC)
  ↓
[Private + Protected Things]  ←  Secured Here
  ↓
Child Class
  ↓
Implements and Uses Secure Stuff
"""

from abc import ABC, abstractmethod
import random

# class SecretSystem(ABC):
#     def __init__(self):
#         self._api_key = "SECRET-123"  # Protected variable
#         self.__password = "hidden-password"  # Private variable

#     @abstractmethod
#     def access_system(self):
#         pass

#     def _internal_log(self, message):
#         print(f"[Internal Log]: {message}")  # Protected method

#     def __hidden_method(self):
#         print("This is a fully private hidden method.")

# class UserAccess(SecretSystem):
#     def access_system(self):
#         print(f"Accessing system with API Key: {self._api_key}")
#         self._internal_log("User accessed the system.")
#         # self._SecretSystem__hidden_method() # Like this I can call the private variable 
#         # Can't call __hidden_method directly because it's private

# user = UserAccess()
# user.access_system()
# user.__hidden_method()  # ❌ Error: can't access private method directly


class CircularList:

    def __init__(self, size=5):
        self.size = size
        self.buffer = []
        self.current_idx = 0

    def add(self, element:str):
        if len(self.buffer) < self.size:
            self.buffer.append(element)
        else:
            self.buffer[self.current_idx] = element
        self.current_idx = (self.current_idx + 1) % self.size

    def get(self):
        return self.buffer


class BankAccount(ABC):
    def __init__(self,account_holder,account_bal,bank_code):
        super().__init__()
        self.account_holder = account_holder
        self._account_bal = account_bal
        self.__bank_code = bank_code
    
    @abstractmethod
    def deposit(self):
        pass 
    
    @abstractmethod
    def withdraw(self):
        pass 
    
    def _log_message(self,message):
        print(f"{self.account_holder} {message}")
    
    def check_account_bal(self):
        print(f"{self.account_holder} having currently {self._account_bal} money in this account")
    
    def __show_secrate_code(self):
        print(f"Bank secrate code is {self.__bank_code} Don't share with anyone")
    

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_bal, bank_code,user_secrate_code):
        super().__init__(account_holder, account_bal, bank_code)
        self.account_number = random.randrange(10000000, 100000000)
        self.user_secrate_code = user_secrate_code
        self.transaction = CircularList(size=3)
    
    
    def deposit(self,money:int):
        if money >0 and type(money)==int:
            self._account_bal += money
            self._log_message(f"This account number {self.account_number} added {money}; total money is {self._account_bal}")
            self.transaction.add("+"+str(money))
        else:
            print("Please enter a valid money ")
    
    def withdraw(self,money:float,user_secrate_code:str):
        if self.user_secrate_code != user_secrate_code:
            print("Please share you secrate code properly ")
            self._log_message(f"The user {self.account_number} given a wrong secrate code! please check with the ac holder")
            return
        if (0< money<=self._account_bal) and (self.user_secrate_code == user_secrate_code):
            self._account_bal -= money
            self._log_message(f"This account number {self.account_number} debited {money}; total money is {self._account_bal}")
            self.transaction.add("-"+str(money))
        else:
            print(" Sir you don;t have suffient balance ")
    
    def apply_interest(self,interest_rate:float=0.03):
        interest = (self._account_bal*interest_rate)
        self._account_bal += interest
        self._log_message(f"This account {self.account_number} interest added {interest}; total money is {self._account_bal}")
    
    def print_transaction(self):
        t_list = self.transaction.get()
        for t in t_list:
            print(f"Your transation is {t}")

s1 = SavingsAccount(account_holder="Humba",account_bal=1000,bank_code="SBI00057",user_secrate_code="1258")
s1.check_account_bal()
s1.deposit(500)
s1.withdraw(100.05,"1258")
s1.check_account_bal()
s1.apply_interest(interest_rate=0.05)
s1.check_account_bal()
s1.print_transaction()
            
        
