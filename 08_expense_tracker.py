
def expense_tracker():
    list=[]
    while True:
        choice=int(input("1. Enter 1 for additing expense to the expense list manager \n 2. Enter 2 for editing expense to the expense manager \n  3. Enter 3 viewing the expenses that you enetered in the expense mnager \n 4. Enter 4 for exiting the program:-\t"))
        if choice==1:
            amount=float(input("Enter the amount of expense"))
            description=input("enter the description of the expense")
            list.append({"amount":amount,"description":description})
            for index, item in enumerate(list, start=1):
                print(f"{index}. {item}")
            print(f"the expense tracker list like this :-\n {list}\n after the entry of amount{amount}:-{description}")
        elif choice==2:
            for index, item in enumerate(list,start=1):
                print(f"{index}.{item}")
            edit=int(input("enter the entry of the expense that you wanted to edit"))
            list.pop(edit-1)
            amount=int(input("enter the amount"))
            description=input("enter the description")
            list(edit+1,{"amount":amount,"description":description})
            print(f"the new updated list after editing list is with {amount}:-{description}")
            for index,item in enumerate(list,start=1):
                print(f"{index}.{item}")
        
        
        elif choice==3:
            print("the expense tracker list looks as follows")
            for index, item in enumerate(list,start=1):
                print(f"{index}.{item}")
        elif choice==4:
            print("thanks for using")
            break
        else:
            print("enter a valid choice")
expense_tracker()

