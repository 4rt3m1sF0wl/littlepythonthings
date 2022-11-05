# Tictactoe game
# loop of sequence
restart = "y"
while restart.upper() != 'Y' or restart.upper() != "YES":
    print('Welcome. This is the tictactoe game for python.')

    # These are all the variables the code should need to start off
    # Unplayed and played are the moves left and used, and board is all the spaces on the ttt board
    player = -1
    unplayed = ['1','2','3','4','5','6','7','8','9']
    board = ['1','2','3','4','5','6','7','8','9']
    played = []
    winstate = False

    #function to check if a winstate is reached, checks all positions (very bloated lol)
    def winstatefunc():
        if bool(board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or bool(board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or bool(board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or bool(board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or bool(board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or bool(board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or bool(board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or bool(board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
            return input('\nPlayer 2 Wins!! Good job Player 2. Try again? y/n:')
            return True

        elif bool(board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or bool(board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or bool(board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or bool(board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or bool(board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or bool(board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or bool(board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or bool(board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
            restart = input('\nPlayer 1 Wins!! Good job Player 1. Try again? y/n:')
            return True
        elif unplayed == []:
            restart = input("It's a Tie... try again ? y/n:")
            return True

    print('This is the board\n' '||', board[0], board[1], board[2],'||\n||', board[3], board[4], board[5], '||\n||', board[6], board[7], board[8],'||' )

    # This loop allows players 1 and 2 to make moves until one player wins
    while winstate != True:
        player = player + 1

       # Player 1 loop, checking if input move is a real move and has not yet been taken
        if player%2 == 0:
            while True:
                move = input("player 1's turn! enter 1 through 9:")
                if move in played:
                    print(f'This move has been played. Play one of these: {unplayed}')
                    continue
                elif move in unplayed:
                    board[int(move)-1] = 'X'
                    played.append(move)
                    unplayed.remove(move)
                    print('||', board[0], board[1], board[2],'||\n||', board[3], board[4], board[5], '||\n||', board[6], board[7], board[8], '||')
                    break
                else:
                    print('make sure that you played a move (anything between 1 and 9). Please try again')
                    continue

            # did they win ??       
            winstate = winstatefunc()           

        # Player 2 loop
        elif player%2 != 0: 
            while True:
                move = input("player 2's turn! enter 1 through 9:")
                if move in played:
                    print(f'This move has been played. Play one of these: {unplayed}')
                    continue
                elif move in unplayed:
                    board[int(move)-1] = 'O'
                    played.append(move)
                    unplayed.remove(move)
                    print('||', board[0], board[1], board[2],'||\n||', board[3], board[4], board[5], '||\n||', board[6], board[7], board[8], '||')
                    break

                else:
                    print('make sure that you played a move (anything between 1 and 9). Please try again')
                    continue

            # did they win ??
            winstate = winstatefunc()
