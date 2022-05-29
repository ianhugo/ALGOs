# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

# Your previous Plain Text content is preserved below:


"""
Context: Apple Business team
Problem: Want Revenue of the Day

Input: Account information
DS: Account object, property with balance information

Output: Sum of account balances
DS: float

Solution v1.0 (Brute)
1. Iterate through each object, get property balance
2. Increment var "Total_Account_Balance"


Example 1:
account_list = [<Account_1>, <Account_2>, <Account_3>]
"""

class Account:

    def __init__(self, balance=0):
        self.balance = balance

def sum_account_balances(account_list):


    if account_list is not list:
        return "Account list input should be list!"


    summed_balance = 0
    accounts_error_list = []

    for account in account_list:
        if account is not Account:
            accounts_error_list.append(account)

        #check if propertty value valid
        account_balance = account.balance
        if account_balance is not int or account_balance is not float:
            accounts_error_list.append(account)
        
        summed_balance+= account.balance
    
    return summed_balance, accounts_error_list


account_list = [Account(10), Account(11), Account(12)]

summed_balance = sum_account_balances(account_list)

print(f"Total of balances from Accounts: {summed_balance}")
