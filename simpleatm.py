    
def atm():    
    print("ATM")
    print("-"*25)
    print('1 | Deposit')
    print('2 | With Drawal')
    print('3 | Check Balance')
    print("-"*25)
    
    atm = int(input('Choose a transaction\t:'))
    if atm == 1:
        total = float(input('input the total cash you want to deposit :'))
        print('Transaction Complete')
    elif atm == 2:
        deposit = float(input('input the amount you want to withdraw\t: '))
        print('Your balance is Insufficient')
    elif atm == 3:
        print('RP 0')
    else:
        print('Sorry, the option you choose does not exist.Please try another')
atm()    