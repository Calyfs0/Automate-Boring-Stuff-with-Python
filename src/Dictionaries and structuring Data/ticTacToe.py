def initialize_board():
    return {
        'top-L': ' ',
        'top-M': ' ',
        'top-R': ' ',
        'mid-L': ' ',
        'mid-M': ' ',
        'mid-R': ' ',
        'low-L': ' ',
        'low-M': ' ',
        'low-R': ' ',
    }


def print_board(board):
    """Prints the current state of the board."""
    print(f" {board['top-L']} | {board['top-M']} | {board['top-R']} ")
    print('---+---+---')
    print(f" {board['mid-L']} | {board['mid-M']} | {board['mid-R']} ")
    print('---+---+---')
    print(f" {board['low-L']} | {board['low-M']} | {board['low-R']} ")


def check_winner(board):
    winning_combinations = [
        ['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L'],
    ]

    # Check for each winning combination
    for combination in winning_combinations:
        if (
            board[combination[0]]
            == board[combination[1]]
            == board[combination[2]]
            != ' '
        ):
            return board[combination[0]]  # Return 'X' or 'O' as the winner

    return None  # No winner yet


def get_player_move(options):
    """Prompts the player to make a move and returns the chosen position."""
    while True:
        move = input("Enter your move: ")
        if move in options:
            return move
        print(f"Invalid move. Please choose from: {options}")


# Main method
def main():
    try:
        board = initialize_board()
        options = list(board.keys())
        turn = 'X'
        for i in range(9):
            print_board(board)
            print(f'You have options: {options}')
            print(f"Turn for {turn}. Move on which space?")

            move = get_player_move(options)
            options.remove(move)
            board[move] = turn

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f'{winner} wins!')
                break

            turn = 'O' if turn == 'X' else 'X'

        else:
            print_board(board)
            print('It\'s a tie!')
    except KeyboardInterrupt:
        print("\nLet's play next time.\nCiao!!!")


if __name__ == '__main__':
    main()
