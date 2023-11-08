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

def ask_input(current_player):
   prompt = f'Player {current_player}, please enter row and column numbers separated by a comma (e.g., 1,1):\n'
   while True:
       try:
           player_input = input(prompt)
           row, col = [int(x) - 1 for x in player_input.split(',')]
           if 0 <= row <= 2 and 0 <= col <= 2:
               return row, col
           else:
               print('Invalid input. Row and column numbers must be between 1 and 3. Please try again.')
       except ValueError:
           print('Invalid input. Please enter valid numbers separated by a comma.')


# if this program is run directly, don't want this part to run when it is imported
if __name__ == '__main__':
    board = get_empty_board()
    current_player = 'X'
    winner = None

    while winner is None:
        print_board(board)
        row, col = ask_input(current_player)
        winner = check_winner(board)

        if board[row][col] is None:
            board[row][col] = current_player
        else:
            print('Invalid move. That position is already taken. Please try again.')
            continue

        winner = check_winner(board)
        if winner is not None:
            print(f'Player {winner} wins!')
            break
        current_player = switch_player(current_player)

    #check winner
    #check if game is draw
    #print the winner