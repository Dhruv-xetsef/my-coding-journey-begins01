import math
def calculator():
    choice=int(input("enter 1 for addition\n enter 2 for subtraction \n enter 3 for multiplication \n enter 4 for division \n enteer 5 for logrethmic function :- \t"))
    print(f"you choose {choice}")
    num1=int(input("\033[0menter number 1\033[0m (if logerthmic function is to be choosen then this is base):-\t"))
    num2=int(input("\033[0menter number 2\033[0m:- \t "))
    if choice==1:
        sum==num1+num2
        print(f"the sum of the two given numbers is {sum}")
    elif choice==2:
        difference=num1-num2
        print(f"the difference of the given two numbers is {abs(difference)}")
    elif choice==3:
        product=num1*num2
        print(f"the product of the two numbers is{product}")
    elif choice==4:
        if num2!=0:
            division=num1/num2
            print(f"the division of the following two numbers is {division}")
        else:
            print("division by 0 is not permitted")
    elif choice==5:
        if num1>0:
            log=math.log(num1,num2)
            print(f"the logerithm of these give two numbers is {log}")
        else:
            print("base of the logerithmic function can't be 0 or nagetive")
    else:
        print("you entered a invalid choice")
calculator()