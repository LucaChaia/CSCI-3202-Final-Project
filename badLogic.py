import random

winner = ""

pits_per_player = 3
stones_per_pit = 2

board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones 
ai = False #our human player will go against an algorithm that chooses moves randomly
current_player = 1
player = True #the player character will be human and not another random algorithm
ai_wins = 0
ai_losses = 0
#moves = []
p1_pits_index = [0, pits_per_player-1]
p1_mancala_index = pits_per_player
p2_pits_index = [pits_per_player+1, len(board)-1-1]
p2_mancala_index = len(board)-1

# Zeroing the Mancala for both players
board[p1_mancala_index] = 0
board[p2_mancala_index] = 0

won = False

def newGame(flip_ai):
    global board, ai, player, won, ai_wins, ai_losses

    board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones
    board[p1_mancala_index] = 0
    board[p2_mancala_index] = 0
    
    if flip_ai:
        ai = not ai
    else:
        player = not player
    
    current_player = 1

    won = False
    ai_wins = 0
    ai_losses = 0

def display_board():
    player_1_pits = board[p1_pits_index[0]: p1_pits_index[1]+1]
    player_1_mancala = board[p1_mancala_index]
    player_2_pits = board[p2_pits_index[0]: p2_pits_index[1]+1]
    player_2_mancala = board[p2_mancala_index]
    
    text = '|    |  {}   {}   {}  |    |\n| {} |                | {} |\n|    |  {}   {}   {}  |    |'.format(
                            board[6], board[5], board[4], board[len(board)-1], board[3], board[0], board[1], board[2]
            )
    print(text)
    return text


def valid_move(move):
    if move <= 0: 
        print("Invalid move\n")
        return False
    elif current_player == 2:
        """ Indices visualization
        1, 1, 1, 1, mancala, 2, 2, 2, 2, mancala
        0  1  2  3     4     5  6  7  8     9
        """
        move += pits_per_player
        if move >= len(board) or move == p2_mancala_index:
            print("Invalid move\n")
            return False
    else:
        move -= 1
        if move >= pits_per_player or move == p1_mancala_index:
            print("Invalid move\n")
            return False
    
    if board[move] <= 0: #should never be less than zero, but I figure that the failsafe is worth it
        print("Invalid move\n")
        return False
    
    return True

def random_move_generator():
    moves = []
    if current_player == 1:
        start = 0
        end = pits_per_player
        offset = 0
    else:
        start = pits_per_player + 1
        end = len(board)
        offset = pits_per_player
    
    for i in range(start, end):
        if board[i] != 0:
            moves.append(i - offset)
    
    return moves

def random_valid_move():
    moves = random_move_generator()
    index = random.randint(0, len(moves) - 1)
    return moves[index]

def play(pit):
    global current_player, board
    
    print(f"Player {current_player} chose pit: {pit}")
    
    if not winning_eval() and valid_move(pit):
        moves.append((current_player, pit))
        
        if current_player == 2:
            pit += pits_per_player
        else:
            pit -= 1
        
        stones = board[pit]
        i = pit
        board[pit] = 0
        
        # this can be optimized
        while stones > 0:
            if (current_player == 1 and i == p2_mancala_index) or (current_player == 2 and i == p1_mancala_index):
                #don't drop stones into enemy's mancala
                continue
            
            board[i] += 1
            stones -= 1
            
            if i == (len(board) - 1):
                i = 0
            else:
                i += 1
        
        if board[i-1] == 1: #then the pit we dropped our last stone was empty
            

        if not winning_eval():
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
    
    return winning_eval()

def winning_eval():
    global won, ai_wins, ai_losses, winner
    
    if won:
        return True
    
    pits1 = board[p1_pits_index[0]: p1_pits_index[1]+1]
    p1_score = 0
    pits2 = board[p2_pits_index[0]: p2_pits_index[1]+1]
    p2_score = 0
    
    for i in range(0,len(pits1)):
        if current_player == 1 and pits1[i] != 0:
            return False
        elif current_player == 2 and pits2[i] != 0:
            return False
        p1_score += pits1[i]
        p2_score += pits2[i]
    
    won = True
    if(p1_score > p2_score):
        winner = 'Player'
        ai_losses += 1
    elif(p1_score < p2_score):
        winner = 'Enemy'
        ai_wins += 1
    else:
        winner = 'Tie'
    
    return True

def calc_rate():
    if ai_wins == 0 and ai_losses == 0:
        return "100"
    return str((ai_wins/(ai_wins+ai_losses)) * 100)

def evalWinner():
    if winner == "Player":
        return "You win!"
    elif winner == "Enemy":
        return "Enemy wins!"
    elif winner == "Tie":
        return "Tie!"
    else:
        return f"Error in evalWinner if statement. winner == {winner}"












