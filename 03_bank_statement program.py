def bank():
    print("welcome😊😎 \n this is a bank statement programe")
    bank_balance=float(input("enter amount of money in your account \n $"))
    while True:
        action=int(input("enter 1 for depositing amount \n enter 2 for withdrawing the amount \n enter 3 for checking balance \n enter 4 for exit \n please enter your choice \t"))
        if action==1:
            amount=float(input("enter the amount you want to deposite"))
            if amount>0:
                new_balance=amount+bank_balance
                bank_balance=new_balance
                print(f"your new account balance is {new_balance} after deposite of {amount}")
            else:
                print ("enter valid choice that is grater amount that is more than 0")
        elif action==2:
            amount=float(input("enter the amount you want to withdraw \tab"))
            if amount>0 and bank_balance>=amount:
                new_balance=bank_balance-amount
                bank_balance=new_balance
                print(f"your new amount in bank is {new_balance} after withdrawal of {amount}")
            else:
                print("enter valid choice that is greater than that of the0 amount ")
        elif action==3:
            print(f"the amount that is available i your bank account is {bank_balance}")
        elif action==4:
            print("thanks for choosing our services")
            break
        else:
            print("please enter valo=id choice")
bank()
