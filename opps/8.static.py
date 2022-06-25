# There are mainly two types of variable in opps. 
'''
1) instance varible- 
    has differnet value for each of object from same class.

2) static variable-
    has same value for all objects from a same class.

'''










import random
 
class ATM():
    
    __counter = 1
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.sno = ATM.__counter
        ATM.__counter = ATM.__counter + 1
        self.transaction()
    
    @staticmethod
    def get_counter():
        print(ATM.__counter)
    
    @staticmethod
    def set_counter(new):
        ATM.__counter = new
        
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Nu.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: Nu.", self.balance)
        print()
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:
                
                option = int(input("Enter 1, 2, 3, 4 or 5:\n"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    self.account_detail()
                elif option == 2:
                    self.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    self.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    self.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Nu.{self.balance}  
              counter : {self.sno}                  
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    break
                 

#########################################################################################

# sbi = ATM("sbi", "123")
# print(sbi.name)

# pnb = ATM("pnb", "1234")
# print(pnb.name)

ATM.set_counter(5)
ATM.get_counter()

sbi = ATM("sbi", "123")
print(sbi.name)

pnb = ATM("pnb", "1234")
print(pnb.name)

 
