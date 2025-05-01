import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 6,
    "B": 6,
    "C": 6,
    "D": 3
}

symbol_value = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

def check_win(columns, lines, bet, values):
    winnings = 0
    win_line = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            win_line.append(line + 1)

    return winnings, win_line
def get_slot_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

        
def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be more than 0")
        else:
            print("Please enter a number.")

    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on : (2-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 2 <= lines <= MAX_LINES:
                break
            elif lines > MAX_LINES:
                print("lines must be less than 3")
            elif lines < 2:
                print("Shane hai kya bhai")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def game(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You don't have enough money to bet that amount.")
            print(f"Your current balance is only {balance}.")

        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet : ${total_bet}")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, win_line = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines : ", *win_line)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        if balance != 0:
            spin = input("Press enter to play (q to quit)")
            if spin == "q":
                break
            else:
                balance += game(balance)
        else:
            print("You're broke now")
            break

    print(f"You left with ${balance}")


main()



# if len(user_list)==3:
            #     if user_score/user_input==3:
            #         print("A wild Sachin appeared")
            #         print("Arey ae vedya kuch aur daal na")
            # if len(user_list)==4:
            #     if user_score/user_input==4:
            #         print("A wilder Sachin has appeared")
            #         print("arey ae vedya bhenchos bat ka grip nikaal ke na seedha bat teri gaand mai daalega")
            # if len(user_list)==5:
            #     if user_score/user_input==5:
            #         print("A wilder Dhoni has appeared")
            #         print("Abey Bhosdike sunn, beech raaste mai kapde utar ke teri gaand mai helicopter shot maarunga")