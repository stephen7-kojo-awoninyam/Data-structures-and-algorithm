import json

account = {}

def Account(AccountNumber,InitialDeposit):
    """
    Returns a dictionary having a key of account number and a value of initial deposit
    
    """
    account = {}
    try:
        if InitialDeposit <=0 and AccountNumber <= 0:
            raise ValueError
        account[str(AccountNumber)] = InitialDeposit
    except ValueError:
        print("invalid Deposite")
            
    return account


def Deposit(account,accountNumber, deposit):
    """Returns a new balance by adding the deposit to the imitial deposit"""
    
    account[accountNumber] = account[accountNumber] + deposit
    
    return account[accountNumber]

def Withdraw(account,accountNumber,withdraw):
    """Returns a new dictionary after withdrawing some from the deposit"""
    
    account[accountNumber] = account[accountNumber]- withdraw
    
    return account[accountNumber]

def CheckBalance(account,accountNumber):
    """Returns an amount within a given account"""
    return account[accountnumber]

def main():
    while True:
        print("""""
            =======================================================
            
            1. CREATE A NEW ACCOUNT
            2. DEPOSIT MONEY INTO AN EXISTING ACCOUNT
            3. WITHDRAW MONEY FROM AN ACCOUNT
            4. CHECK BALANCE 
            5. EXIT
            
            =======================================================

            """)
        number = int(input("Choose an from the above: "))

        if 1 <= number <= 5:
            
            
            if number == 1:
                
                account_name = int(input("Enter your preferred account number: "))
                initial_amount = int(input("Enter your initial amount to deposit: "))
                account = Account(account_name,initial_amount)
                print("New account created successfully")
                print(account)
                
            elif number == 2:
                
                account_number = int(input("Enter your account number: "))
                amount_to_deposit = int(input("Enter amount to deposite: "))
                balance = Deposit(account,account_number,amount_to_deposit)
                print("Your new balance is:",balance)
                
            elif number == 3:
                account_number = int(input("Enter your account number: "))
                amount_to_withdraw = int(input("Enter amount to deposite: "))
                balance = Withdraw(account,account_number,amount_to_withdraw)
                print("Your new balance is:",balance)
                
            elif number == 4:
                account_number = int(input("Enter your account number"))  
                print("Your new balance is:",CheckBalance(account,account_number))
            else:
                break     
                        
        else:
            print("choose within the range of 1 and 4 to choose option")  
            
if __name__ == "__main__":
    main()                                        
                                
                                
                                    
                            
                        
                        

            
            
            
            
        