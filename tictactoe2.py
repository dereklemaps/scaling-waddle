board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def game_on():
    choice = ''
    while choice not in ('Y', 'N'):
        choice = input('Would you like to keep playing? Y or N: ')
        if choice not in ('Y', 'N'):
            print('Sorry not a valid choice')
    if choice.upper() == 'Y':
        return True
    elif choice.upper() == 'N':
        return False

def display(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_character():
    choice = ''
    while choice not in ('X', 'O'):
        choice = input('Choose your character - X or O: ').upper()
        if choice not in ('X', 'O'):
            print('Sorry not a valid choice')
    return choice

def player_slot():
    slot = 'wrong'
    within_range = False
    while slot.isdigit() == False or within_range == False:
        slot = input('Choose your position 1-9: ')
        if slot.isdigit() == False:
            print('Sorry not a valid choice')
        elif slot.isdigit():
            if int(slot) in range(1,10):
                within_range = True
            else:
                print('Sorry not a valid choice')
    return int(slot)

def space_check(slot):
    spaces = []
    if slot in spaces:
        print('Sorry slot is filled')
    else:
        spaces.append(slot)

def check_board(board, choice, slot):
    board[slot] = choice
    
def win_check(board, choice):    
    if (board[7] == board[4] == board[1]) or (board[8] == board[5] == board[2]) or (board[9] == board[6] == board[3]) or (board[7] == board[8] == board[9]) or (board[4] == board[5] == board[6]) or (board[1] == board[2] == board[3]) or (board[7] == board[5] == board[3]) or (board[9] == board[5] == board[1]):
        print(f'{choice} wins!')
        gameon = False
    else:
        return board

gameon = True

while gameon:
    display(board)
    choice = player_character()
    slot = player_slot()
    space_check(slot)
    check_board(choice, slot)
    win_check(board, choice)
    display(board)
    gameon = game_on()