import random

def game():
    user=0
    comp=0
    dict={0 : "Rock",
          1 : "Paper",
          2 : "Scissors"}
    
    while user<=5 or comp<=5: 
        if user==5:
            print("You won the game! Press q to quit or r to restart:")
            input1=input(" ")
            if input1=="r" or input1=="R":
                print("\nThe game has been reset")
                user=0
                comp=0
            elif input1=="q" or input1=="Q":
                print("Thank you for playing!")
                exit()
            else:
                exit()
        elif comp==5:
            print("Computer won the game! Press q to quit or r to restart:")
            input1=input(" ")
            if input1=="r" or input1=="R":
                print("\nThe game has been reset")
                user=0
                comp=0
            elif input1=="q" or input1=="Q":
                print("Thank you for playing!")
                exit()
            else:
                exit()      
        
        print("Enter 0 for Rock, 1 for Paper, 2 for Scissors") 
        user_input = input("User:")
        if user_input=="0" or user_input=="1" or user_input=="2":
            user_input=int(user_input)
        else:
            print("Please Enter a valid Input!")
            continue

        
        comp_input=random.randint(0,2)
        print(f"Computer:{comp_input}")
        print(f"\nYou chose {dict.get(user_input)}, Computer chose {dict.get(comp_input)}")

        if user_input==0 and comp_input==0:
            print(f"Tie! Your score:{user} Computer score:{comp}\n")
        elif user_input==0  and comp_input==1:
            comp+=1
            print(f"Computer wins a point! Your score:{user} Computer score:{comp}\n")
        elif user_input==0 and comp_input==2:
            user+=1
            print(f"You win a point! Your score:{user} Computer score:{comp}\n")
        elif user_input==1 and comp_input==0:
            user+=1
            print(f"You win a point! Your score:{user} Computer score:{comp}\n")
        elif user_input==1 and comp_input==1:
            print(f"Tie! Your score:{user} Computer score:{comp}")
        elif user_input==1 and comp_input==2:
            comp+=1
            print(f"Computer wins a point! Your score:{user} Computer score:{comp}\n")
        elif user_input==2 and comp_input==0:
            comp+=1
            print(f"Computer wins a point! Your score:{user} Computer score:{comp}\n")
        elif user_input==2 and comp_input==1:
            user+=1
            print(f"You win a point! Your score:{user} Computer score:{comp}\n")
        elif user_input==2 and comp_input==2:
            print(f"Tie! Your score:{user} Computer score:{comp}\n")
game()

