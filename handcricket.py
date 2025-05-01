import random

decision = ""  
comp_decision = "" 
user_score=0
comp_score=0
user_list=[]

opp_teams = ["Crocodiles", "DoFlamingos", "Magellen Eleven", "Moria Shadows", "Dragons", "Mermaid Lords"]
opp_team = random.choice(opp_teams)
print("""Welcome to the game of cricket!
Enter the name of your team""")
name = input("> ")
print("Enter your name.")
user = input("> ")
print(f"{user}\'s {name} is playing against {opp_team}!")
def toss():
    global decision, comp_decision  # Declare the variables as global within the function

    choice = input("odd or even: ")
    if choice.lower() == "odd" or choice.lower() == "even":
        while True:
            choice_num = input("Enter a number between 1 and 10:")
            choice_comp = random.randint(0, 10)
            if choice_num=="1" or choice_num=="2" or choice_num=="3" or choice_num=="4" or choice_num=="5" or choice_num=="6" or choice_num=="7" or choice_num=="8" or choice_num=="9" or choice_num=="10":
            
                print("Computer chose: " + str(choice_comp))
                tosss = int(choice_num) + int(choice_comp)
                if choice.lower() == "odd":
                    if tosss % 2 == 0:
                        print('Sorry you lost!')
                        comp_decision = random.choice(["Bat", "Bowl"])
                        print("Computer chose to: " + comp_decision)
                    else:
                        print("Congrats you won!")
                        decision = input("Bat or Bowl: ")
                else:
                    if tosss % 2 == 0:
                        print("Congrats you won!")
                        decision = input("Bat or Bowl: ")
                    else:
                        print('Sorry you lost!')
                        comp_decision = random.choice(["Bat", "Bowl"])
                        print("Computer chose to: " + comp_decision)
                break
            else:
                print("Please enter a valid number!")
                continue
            
    else:
        print("Please type either odd or even: ")
        toss()


toss()

def user_bat():
    global user_score,comp_score,user_list
    if decision.lower()=="bat" or comp_decision.lower()=="bowl":
        print("You are Batting..\n")
        while True:
            user_input=int(input("Enter a number between 1 to 10: "))
            user_list.append(user_input)
            comp_input=random.randint(0,10)
            if user_input==comp_input:
                print("Computer chose: "+str(comp_input))
                print("You are out! \n")
                print("Score is :"+str(user_score))
                Target=user_score+1
                print("Target is: "+str(Target))
                break
            else:
                user_score=user_score+user_input
                if len(user_list)==3:
                    if user_score/user_input==3:
                        print("A wild Sachin appeared")
                        print("Arey ae vedya kuch aur daal na")
                if len(user_list)==4:
                    if user_score/user_input==4:
                        print("A wilder Sachin has appeared")
                        print("arey ae vedya")
                if len(user_list)==5:
                    if user_score/user_input==5:
                        print("A wild Sachin has appeared")
                        print("arey ae vedya kuch aur daal na")
                print("Computer chose: "+str(comp_input))
                print("Score is :"+str(user_score)+"\n")
        print("\nYou are now Bowling..")
        while True:
            if comp_score>=Target:
                print("Computer Won!")
                exit()
            else:
                comp_input=random.randint(0,10)
                user_input=int(input("Enter a number between 1 to 10: "))
                if user_input==comp_input:
                    print("Computer chose: "+str(comp_input))
                    print("Computer is out! \n")
                    print("Score is :"+str(comp_score))
                    print("You Won!")
                    exit()
                else:
                    comp_score=comp_score+comp_input
                    print("Computer chose: "+str(comp_input))
                    print("Score is :"+str(comp_score)+"\n")

user_bat()

def user_bowl():
    global user_score,comp_score
    if decision.lower()=="bowl" or comp_decision.lower()=="bat":
        print("You are Bowling..\n")
        while True:
            user_input=int(input("Enter a number between 1 to 10: "))
            comp_input=random.randint(0,10)
            if user_input==comp_input:
                print("Computer chose: "+str(comp_input))
                print("Computer is out! \n")
                print("Score is :"+str(comp_score))
                Target=comp_score+1
                print("Target is: "+str(Target))
                break
            else:
                comp_score=comp_score+comp_input
                print("Computer chose: "+str(comp_input))
                print("Score is :"+str(comp_score)+"\n")
        print("\nYou are now Batting..Target is "+str(Target))
        while True:
            if user_score>=Target:
                print("You Won!")
                exit()
            else:
                comp_input=random.randint(0,10)
                user_input=int(input("Enter a number between 1 to 10: "))
                if user_input==comp_input:
                    print("Computer chose: "+str(comp_input))
                    print("User is out! \n")
                    print("Score is :"+str(user_score))
                    print("Computer Won!")
                    exit()
                else:
                    user_score=user_score+user_input
                    print("Computer chose: "+str(comp_input))
                    print("Score is :"+str(user_score)+"\n")
user_bowl()
    




