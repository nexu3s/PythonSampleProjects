print("hello to my quiz game !")

while True :

    playing = input("Do you want to play this game? (y/n) ").lower()

    # cheack playing or not
    if playing == "y":
        print("Alright lets play!")
        print("=======================================")
        
        #start the game
        score = 0

        # start questions
        question = input("what is the cpu stands for ? ").lower()

        if question == "central processing unit":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
    
        question = input("what is the ram stands for ? ").lower()

        if question == "random access memory":
            print("correct!")
            score += 1
        else:
            print("incorrect!")


        question = input("what is the psu stands for ? ").lower()

        if question == "power supply unit":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
        # stop questions

        # process the answers
        score = round(score / 3 * 100, 2)
        print(f"you answered {score}% of questions correctly")
        break
    
    # cheack playing or not  
    elif playing == "n":
        print("sorry to left you :)")   
        break
    else :
        print("please enter the correct answer (y/n)")
        print("=======================================")
        
    else : 
        print("nima is very kuni")
