import random 

while True:

    number = random.randint(1,11)
    guess = 0 
    attempts = 0 



    print(" ---------Welcome to the number guessing game ---------")
    print("The computer is thinking of a number betweeen 1 and 11 .")
    while guess != number:
    
        guess = int(input("Enter your guess : "))
        attempts += 1 

        if guess < number:
            print("Too low ")
        elif guess > number:
            print("Too high") 
        else:
            print("That's correct . You have guessed the right number .")
    
            print()
            print(f"You have guessed the number in {attempts} attempts ")
            break

    play_again=input("Do you want to play agian : ( Yes/No : ) ").lower()

    if play_again != "yes":
        print("Thanks for playing the game . ")
        break 
        
