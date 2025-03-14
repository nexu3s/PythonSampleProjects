import random

print("hi,i generate random number and you guess !")

while True:
    # enter top range of random number
    top_of_range = input("chooose random number grather than 0: ")

    if top_of_range.isdigit():

        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("enter a number greather than 0 next time.")  
            continue
       
        # generate random number from 0 to top range
        random_number = random.randint(0, top_of_range)
       
        # make a guess
        guesses = 0
        
        while True:
            guesses += 1
            user_guess = input("make a guess: ")
            
            if user_guess.isdigit():

                user_guess = int(user_guess)

            else:
                print("invalid! please guess a number next time!")
                continue

            if user_guess == random_number:
                print("nice! you found the number.")

                print(f"you try {guesses} time to found the number! ")
                break
            
            elif user_guess > random_number:
                print("number is greather than random number !")
            else: 
                print("number is smaller than random number !")

        quit()
    else:
        print("please enter a number to start the game next time.")
        