import random

def main():
    global balance
    print("WELCOME TO ALI'S CASINO")
    options=["Roulette","Blackjack","Slot","Poker"]
    try:
        balance = int(input("How much is your deposit: "))
    except ValueError:
        balance=int(input("Invalid input! Please enter an integer value: "))
    
    game=input(f"Choose a game to play from the following {options} :")
    if game.lower()=="roulette":
        roulette()
    elif game.lower()=="blackjack":
        blackjack()
    elif game.lower()=="slot":
        slot()
    elif game.lower()=="poker":
        poker()
    else:
        print("Invalid Input! You have been banished from this elite casino!")


def roulette():
    print("You are now playing ROULETTE")


def blackjack():
    global bet,balance
    print("You are now playing BLACKJACK")
    bet=int(input("How much do you wanna bet: "))
    while(bet>balance):
        print("Tf you on? German Weed?")
        bet=int(input("How much do you wanna bet: "))
    card1=random.randint(1,13)
    card2=random.randint(1,13)
    total=card1+card2
    print(f"Card 1: {card1} Card 2: {card2}")
    print(f"Total: {total}")
    if card1+card2<21:
        dec=input("Hit or Stand: ")
        while(dec.lower()=="hit"):
            card=random.randint(0,13)
            if card==11:
                print("Card: Jack")
                total+=card
                if total>21:
                    print("BUSTEDDDDDDDDD SUCKERRR")
                    balance=balance-bet
                    print(f"Your balance is: {balance}")
                    dec="stand"
                    break
                dec=input("Hit or Stand: ")
            if card==12:
                print("Card: Queen")
                total+=card
                if total>21:
                    print("BUSTEDDDDDDDDD SUCKERRR")
                    balance=balance-bet
                    print(f"Your balance is: {balance}")
                    dec="stand"
                    break
                dec=input("Hit or Stand: ")
            if card==13:
                print("Card: King")
                total+=card
                if total>21:
                    print("BUSTEDDDDDDDDD SUCKERRR")
                    balance=balance-bet
                    print(f"Your balance is: {balance}")
                    dec="stand"
                    break
                dec=input("Hit or Stand: ")
            if card==1:
                print("Card: Ace")
                total+=card
                if total>21:
                    print("BUSTEDDDDDDDDD SUCKERRR")
                    balance=balance-bet
                    print(f"Your balance is: {balance}")
                    dec="stand"
                    break
                dec=input("Hit or Stand: ")
            else:
                print(f"Card: {card}")
                total+=card
                if total>21:
                    print("BUSTEDDDDDDDDD SUCKERRR")
                    balance=balance-bet
                    print(f"Your balance is: {balance}")
                    dec="stand"
                    break
                dec=input("Hit or Stand: ")
        if dec.lower()=="stand":
            dealer()
        print(total)
        print(totalnew)
    else:
        dealer()
            
def dealer():
    global totalnew,balance
    print("Dealer's Turn!")
    card3=random.randint(1,13)
    card4=random.randint(1,13)
    totalnew=card3+card4
    print(f"Card 1:{card3} Card 2:{card4}")
    print(f"Total:{totalnew}")
    choice=random.randint(1,2)
    while(choice==1):
        card=random.randint(0,13)
        if card==11:
            print("Card: Jack")
            totalnew+=card
            if totalnew>21:
                print("BUSTEDDDDDDDDD SUCKERRR")
                balance=balance+bet*2
                print(f"Your balance is: {balance}")
                break
        if card==12:
            print("Card: Queen")
            totalnew+=card
            if totalnew>21:
                print("BUSTEDDDDDDDDD SUCKERRR")
                balance+=bet*2
                print(f"Your balance is: {balance}")
                break
        if card==13:
            print("Card: King")
            totalnew+=card
            if totalnew>21:
                print("BUSTEDDDDDDDDD SUCKERRR")
                balance+=bet*2
                print(f"Your balance is: {balance}")
                break
        if card==1:
            print("Card: Ace")
            totalnew+=card
            if totalnew>21:
                print("BUSTEDDDDDDDDD SUCKERRR")
                balance+=bet*2
                print(f"Your balance is: {balance}")
                break
        else:
            print(f"Card: {card}")
            totalnew+=card
            if totalnew>21:
                print("BUSTEDDDDDDDDD SUCKERRR")
                balance+=bet*2
                print(f"Your balance is: {balance}")
                break
    
        


def slot():
    print("You are now playing SLOT")

def poker():
    print("You are now playing POKER")

main()
