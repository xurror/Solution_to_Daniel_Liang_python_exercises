'''Program to create ATM class'''
import sys

class Account:
    def __init__(self):
        self.__balance = 100.0
        self.__id= 0
        self.__annualInterestRate = 0.0
   
    def getMonthlyInterestRate(self):
        return (self.annualInterestRate/100)/12
  
    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()
 
    def withdraw(self,amount):
        self.__balance=self.__balance-amount
 
    def deposit(self,amount):
        self.__balance=self.__balance+amount
      
    def getBalance(self):
        return self.__balance

class ATMmachine(Account):
    def __init__(self, id):
        super().__init__()
        self.id = id
    def getMainMenu(self):
        return "Main menu \n1: Check balance \n2: Withdraw \n3: Deposit \n4: Exit \nEnter a choice: "
    
    
def main():
    account=[0,1,2,3,4,5,6,7,8,9]
    
    while True:
        id1 = eval(input("Enter an account id: "))
        if id1 in account:
            atmMachine = ATMmachine(id1)
            while True:
                choiceInput = eval(input(atmMachine.getMainMenu()))
                if choiceInput == 1:
                    
                    print("The balance is: ", atmMachine.getBalance())
                    atmMachine.getMainMenu()
                elif choiceInput == 2:
                    d = eval(input("Enter an amount to withdraw: "))
                    atmMachine.withdraw(d)
                    atmMachine.getMainMenu()
                elif choiceInput == 3:
                    d = eval(input("Enter an amount to Deposit: "))
                    atmMachine.deposit(d)
                    atmMachine.getMainMenu()
                elif choiceInput == 4:
                    sys.exit()
                    break
        else:
            print("Incorrect account id!")
        continue

main()
    
         
    
    
    
    