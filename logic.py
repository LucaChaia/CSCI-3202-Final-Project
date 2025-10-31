import random
#random.seed(100)
import json

pits_per_player = 3 #has to be 2 or greater for play() logic to work
stones_per_pit = 2

winner = ""
won = False #has there been *a* winner
ai_wins = 0
ai_losses = 0
num_games = 1;
num_group_games = 1;
total_moves = []
moves = 0

board1 = [stones_per_pit] * (pits_per_player+1)
board2 = [stones_per_pit] * (pits_per_player+1)
mancala_index = pits_per_player
board1[mancala_index], board2[mancala_index] = 0, 0

is_player_one = True #tracks current player

ai = False #our human player will go against an algorithm that chooses moves randomly
player = True #the player character will be human and not another random algorithm

def newGame(flip_ai):
    global board1, board2, ai, player, won, ai_wins, ai_losses, is_player_one, num_plays, moves
    
    if flip_ai:
        ai = not ai
    else:
        player = not player
    
    board1 = [stones_per_pit] * (pits_per_player+1)
    board2 = [stones_per_pit] * (pits_per_player+1)
    board1[mancala_index], board2[mancala_index] = 0, 0
    
    is_player_one = True
    won = False
    
    num_plays += 1
    moves = 0
    
    print('\n\nNew Game:')
    display_board()
    
def play(pit):
    global is_player_one, board1, board2
    
    if is_player_one:
        print(f"Player chose pit {pit + 1}")
    else:
        print(f"Enemy chose pit {pit + 1}")
    
    if valid_move(pit):
        is_board_one = is_player_one #if we're on player two, we're gonna start with board 2
        i = pit
        
        if is_player_one:
            stones = board1[pit]
            board1[pit] = 0
        else:
            stones = board2[pit]
            board2[pit] = 0
        
        while stones > 0:
            i += 1
            if i > pits_per_player:  
                i = 0
            
            if i == mancala_index and is_board_one != is_player_one:
                continue
            elif is_board_one:
                board1[i] += 1
                stones -= 1
            else:
                board2[i] += 1
                stones -= 1
        
        # if i = 0, the last pit it dropped a stone into was its mancala
        if i != mancala_index and is_board_one == is_player_one:
            steal_index = pits_per_player - i - 1
            if is_player_one and board1[i] == 1:
                board1[mancala_index] += (1 + board2[steal_index])
                board2[steal_index] = 0
                board1[i] = 0
            elif board2[i] == 1 and not is_player_one:
                board2[mancala_index] += (1 + board1[steal_index])
                board2[i] = 0
                board1[steal_index] = 0
        
        is_player_one = not is_player_one
        
        return winning_eval()


def valid_move(pit):
    if pit >= 0 and pit < mancala_index and ((is_player_one and board1[pit] > 0) or (not is_player_one
                                                                                   and board2[pit] > 0)):
        return True
    else:
        print("Invalid move\n")
        return False
    
def winning_eval(): 
    global won, ai_wins, ai_losses, winner, board1, board2
    
    player_pits = True
    enemy_pits = True
    
    if won:
        return True
    
    for i in range(0, pits_per_player-1):
        if board1[i] != 0:
            player_pits = False
        if board2[i] != 0:
            enemy_pits = False
        if not (player_pits or enemy_pits):
            break
    
    if player_pits or enemy_pits:
        won = True
        p1_score = board1[mancala_index]
        p2_score = board2[mancala_index]
        for j in range(0,mancala_index): 
            p1_score += board1[j]
            board1[j] = 0
            p2_score += board2[j]
            board2[j] = 0
        board1[mancala_index] = p1_score
        board2[mancala_index] = p2_score
        
        if p1_score > p2_score:
            winner = "Player"
            ai_losses += 1
        elif p1_score < p2_score:
            winner = "Enemy"
            ai_wins += 1
        else:
            winner = "Tie"
    
    return won

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
        return f"Error in evalWinner if statement. Winner == {winner}"

def random_valid_move():
    moves = random_move_generator()
    if not moves:
        print("moves is empty for some reason")
        if winning_eval():
            print("Well, that was the reason.")
        else:
            print("Well, that was not the reason.")
        return 3 #just a random number. If it's not valid, the valid_move func will catch that.
    return random.choice(moves)

def random_move_generator():
    moves = []
    if is_player_one:
        for i in range(0, mancala_index):
            if board1[i] != 0:
                moves.append(i)
    else:
        for i in range(0, mancala_index):
            if board2[i] != 0:
                moves.append(i)
    return moves

def display_board():
    #there is a way to generalize text so that the the number of variables is relative to pits_per_player.
    #I'm not gonna figure it out tho.
    text = '|    |  {}   {}   {}  |    |\n| {} |                | {} |\n|    |  {}   {}   {}  |    |'.format(
                    board2[2], board2[1], board2[0], board2[3], board1[3], board1[0], board1[1], board1[2]
            )
    print(text)
    return text

def resetAI():
    global ai_wins, ai_losses, num_games, num_group_games, moves
    
    j = json.dumps({num_group_games:
                    {
                        "Is the enemy a True AI?": ai,
                        "Number of Games Ran": num_games,
                        "Avg moves per game": mean(total_moves),
                        "Enemy win rate": calc_rate(),
                        "Total Enemy Wins": ai_wins,
                        "Total Enemy Losses": ai_losses
                     }
                    }, indent = 2)
    json.dump()
    
    ai_wins = 0
    ai_losses = 0
    num_games = 0
    moves = []
    
    num_group_games += 1
    
