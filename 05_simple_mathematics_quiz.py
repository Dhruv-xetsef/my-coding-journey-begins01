import random as r
def quiz():
    choice=int(input("this program makes you test your mathematical and analytical skills by simple addition subtration and multiplication problems \n enter 1 for addition \n enter 2 for subtration \n enter 3 for multiplication"))
    
    attempts=int(input('enter number of times you want to play this game'))
    score=0
    for i in range(attempts):
        num1=r.randint(1,100)
        num2=r.randint(1,100)
        user_answer=int(input(f"enter the answe you got \n if first number is {num1}\n second number is{num2} \t"))
        if choice==1:
            correct_answer=num1+num2
            if correct_answer==user_answer:
                print("your answer is correct")
                score=score+1
            else:
                print(f"your answer is incorrect the answer that is correct is {correct_answer}")
        elif choice==2:
            correct_answer=abs(num1-num2)
            if correct_answer==user_answer:
                print("your answer is correct")
                score=score+1
            else:
                print(f"your answer is incorrect the answer that is correct is {correct_answer}")
        elif choice==3:
            correct_answer=num1*num2
            if correct_answer==user_answer:
                print("your answer is correct")
                score=score+1
            else:
                print(f"your answer is incorrect the answer that is correct is {correct_answer}")
        else:
            print("invalid choice enter a valid choice")
quiz()

   