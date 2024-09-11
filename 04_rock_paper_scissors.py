import random
def game():
    attempt=int(input("enter the number of times you want to play"))
    for i in range(attempt):
        computer_choice=random.randint(1,3)
        player_choice=int(input("enter 1 for rock \n enter 2 for paper\n enter 3 for scissors     :-"))
        if computer_choice==1 and player_choice==2:
            print("you choose paper and computer choose rock \n hence you won")
        elif computer_choice==2 and player_choice==3:
            print("you choose scissors and computer choose paper \n hence you won ")
        elif computer_choice==3 and player_choice ==1:
            print("you choose rock and computer choose scissors \n hence you won")
        elif computer_choice==1 and player_choice==3:
            print("you lost \n as  you choose scissors and computer choose rock")
        elif computer_choice==1 and player_choice==1:
            print("you and computer both choose rock \n hence its a tie")
        elif computer_choice==2 and player_choice==1:
            print("you lost \n as you choose rocks and computer choose paper")
        elif computer_choice==2 and player_choice==2:
            print("you and computer both choose paer hence its a tie")
        elif computer_choice==3 and player_choice==2:
            print("you lost")
        elif computer_choice==3 and player_choice==3:
            print("its a tie")
        else:
            print("invalid choice")
game()