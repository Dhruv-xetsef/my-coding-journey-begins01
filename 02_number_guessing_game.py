import random

def game():
    guess = random.randint(1, 100)  
    attempts = int(input("Enter the number of attempts you require to guess the number accurately: "))
    
    for i in range(attempts):
        choice = int(input(f"Attempt {i+1}: Enter a number you guessed (between 1 and 100): "))
        
        if choice == guess:
            print(f"Congratulations! You guessed it correctly. The number is {choice}.")
            break
        elif choice > guess and choice <= 100:
            print("Your choice is greater than the number I picked.")
        elif choice < guess and choice >= 1:
            print("Your choice is smaller than the number I picked.")
        else:
            print("Invalid choice. Please guess a number between 1 and 100.")
        
        if i == attempts - 1:
            print(f"Sorry, you've used all your attempts! The correct number was {guess}.")

game()
