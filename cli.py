from logic import check_winner
def get_empty_board():
    return[
        [None, None, None],[None, None, None],[None, None, None]
    ]

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    return 'X'


def print_board(board):
    for row in board:
        print(row) 


def ask_input():
    current_player = 'X'
    prompt = f'player {current_player} please enter numbers:\n'
    player_input = input(prompt)
    row_col_list = player_input.split(',') #["1", "1"]
    row, col = [int(x) for x in row_col_list]
    return row, col

# if this program is run directly, don't want this part to run when it is imported
if __name__ == '__main__':
    board = get_empty_board()
    row, col = ask_input()
    winner = None

    try:
        row, col = ask_input(current_player)
    except ValueError:
        print('invalid input, try again\n')
        continue

    while winner is None:
        print_board(board)
        current_player = switch_player(current_player)
        rol, col = ask_input(current_player)
        winner = check_winner(board)

    #check winner
    #check if game is draw
    #print the winner