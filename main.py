""" Simple banking functions """

# Creates new account whenever file is run
BALANCE = 0
print('Your Account is Created.')
print('Your Balance = %d' %BALANCE)

def deposit(bal, amt):
    """ To add money to account """
    bal += amt
    print('Your New Balance = %d' %bal)
    return bal

def withdraw(bal, amt):
    """ To withdraw money from account """
    # only if sufficient balance
    if amt > bal:
        print('Insufficient Balance!')
    else:
        bal -= amt
        print('Your Remaining Balance = %d' %bal)
    return bal

def enquiry(bal):
    """ Prints account details """
    print('Your Balance = %d' %bal)

print("1. Deposit\n2. Withdraw\n3. Enquiry\n4. Exit\nEnter your choice: ")
choice = int(input())

# while choice != 4:
#     if choice == 1:
#         amount = int(input('Enter the amount to deposit:'))
#         BALANCE = deposit(BALANCE, amount)
#     elif choice == 2:
#         amount = int(input('Enter the amount to withdraw:'))
#         BALANCE = withdraw(BALANCE, amount)
#     elif choice == 3:
#         enquiry(BALANCE)
#     elif choice == 4:
#         break
#     print("\n1. Deposit\n2. Withdraw\n3. Enquiry\n4. Exit\nEnter your choice: ")
#     choice = int(input())
BALANCE = deposit(BALANCE, 100)
BALANCE = withdraw(BALANCE, 20)
enquiry(BALANCE)
