import random 

options = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0


while True :
    
    player_choose = input("choose rock/paper/scissors or 'Q' to quit game 'R' to see results: ").lower()

    if player_choose == "q" :
        print("bye.see you again !")
        quit()
    
    elif player_choose == "r":
        print(f"you won me {player_wins} time!")
        print(f"i won {computer_wins} time!")   
        break 
    
    elif player_choose not in options:
        continue

    
    random_number = random.randint(0, 2)
    computer_choose = options[random_number]

    if player_choose == "rock" and computer_choose == "paper":
         print(f"you lose! computer choosed {computer_choose} .")
         computer_wins += 1
    
    elif player_choose == computer_choose:
         print(f"tie ! computer choosed {computer_choose} and player choosed {player_choose}")
         computer_wins += 1

    elif player_choose == "paper" and computer_choose == "scissors":
         print(f"you lose! computer choosed {computer_choose} .")
         computer_wins += 1

    elif player_choose == "scissors" and computer_choose == "rock":
         print(f"you lose! computer choosed {computer_choose} .")
         computer_wins += 1
    else:
         print(f"you won ! computer choosed {computer_choose}")
         player_wins += 1

else:
     print("erfan is ulso kuni^2")

