import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { #dictionary structure
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { #dictionary structure
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #check rows user bet on
        symbol = columns[0][line] #symbol in current column
        for column in columns:
            symbol_to_check = column[line] 
            if symbol != symbol_to_check:
                break #goes to check next line
        else:
            winnings += value[symbol] * bet
            winning_lines.append[line + 1]

    return winnings,winning_lines

def get_slot_machine_spin(rows, cols, symbols): #generate symbols in each col based on what's available
    #create list of all posisble values to choose from
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #looping through dictionary
        for i in range(symbol_count):
            all_symbols.append(symbol) #adding vales into symbol list

    columns = [] #storing columns
    for col in range(cols): #generate values inside colums
        column = []
        current_symbols = all_symbols[:] #copying from all_symbols
        for row in range(rows):
            value = random.choice(current_symbols) #picks random value from list
            current_symbols.remove(value) #remove vale so its not picked again
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    #the goal here is to transpose the columns
    for row in range( len(columns[0]) ): #assuming there is something at least in there
        #enumerating gives index as well as item
        for i, column in enumerate(columns): #looping through every single item
            if i != len(columns) - 1:
                print(column[row], end=" | ") #print value at first row of the column
            else:
                print(column[row], end="")
        print() #prints new line char by default

def deposit(): #collects user input
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter num")
    return amount

def get_num_of_lines(): #number of lines, pick 1 to 3 in slot machine
    while True:
        lines = input("Enter num of lines to bet on (1- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid num of lines")
        else:
            print("Please enter num")
    return lines

def get_bet(): 
    while True:
        amount = input("What would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}") #auto converts int to string
        else:
            print("Please enter num")
    return amount

def spin(balance): #instance of game
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You are broke to bet that money, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet} ")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        elif answer == "":
            balance += spin(balance)
        else:
            print("Invalid input. Please press enter or 'q' to quit.")

    print(f"You left with ${balance}")

main()