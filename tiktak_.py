import pandas as pd 
import numpy as np 

"""
    1. Print a game GUI so people know what number to input to get the location of the 3 by 3 matrix 
    2. Ask user to pick the player: X or O 
    3. O goes first, picks a random position 
    4. X goes second, picks a position (ask for position): 
        4.1) if it's the same as O's, error 
    5. keep track of wins: 
        if the same player has chosen any of these combinations, they win: 
            5.1) 1 - 2 - 3 
            5.2) 4 - 5 - 6 
            5.3) 7 - 8 - 9 
            5.4) 1 - 4 - 7 
            5.5) 2 - 5 - 8 
            5.6) 3 - 6 - 9
            5.7) 1 - 5 - 9 
            5.8) 3 - 5 - 7 
    6. At each step, print the tik tak toe matrix that has been played on 
"""
initial_game_grid = np.array(
        [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]
    )

start_game_grid = np.array(
        [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
    )


def print_game_gui(game_grid_, pos, player):
    if pos == 1 and game_grid_[0][0] == ' ': 
        game_grid_[0][0] = player
    elif pos == 2 and game_grid_[0][1] == ' ': 
        game_grid_[0][1] = player
    elif pos == 3 and game_grid_[0][2] == ' ':
        game_grid_[0][2] = player
    elif pos == 4 and game_grid_[1][0] == ' ':
        game_grid_[1][0] = player
    elif pos == 5 and game_grid_[1][1] == ' ':
        game_grid_[1][1] = player
    elif pos == 6 and game_grid_[1][2] == ' ':
        game_grid_[1][2] = player
    elif pos == 7 and game_grid_[2][0] == ' ':
        game_grid_[2][0] = player
    elif pos == 8 and game_grid_[2][1] == ' ':
        game_grid_[2][1] = player
    elif pos == 9 and game_grid_[2][2] == ' ':
        game_grid_[2][2] = player
    else:
        print("error: not an acceptable position.")
    
    return game_grid_
    
    
    
print(initial_game_grid)


# GAME START: player chooses their character 
player_choice = input("Which player do you want to be? O or X: ")

# add a try and catch for if they enter o or x (lower case)

if player_choice == 'O':
    computer_choice = 'X'
else:
    computer_choice = 'O'
    

round_num = 0

print("This is round ", round_num + 1, '.')


def decide_player():
    """ search through the grid, and count how many X's and O's there are 
        the one that has the fewer is the one who should play 
    """
    x_player = 0
    o_player = 0 
    
    for i in range(3):
        for j in range(3):
            if game_grid[i][j] == 'X':
                x_player += 1
            elif game_grid[i][j] == 'O':
                o_player += 1 
            else: #it's empty 
                continue
    
    which_player = ''
    if x_player > o_player:
        which_player = "O"
    elif x_player < o_player:
        which_player = "X"
    else: 
        which_player = "O"
        
    return which_player
    
    
start_game_grid = np.array(
        [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
    )

# O player goes first 

if player_choice == 'O':
    player_position = int(input("Which position do you want to play? "))
    game_grid = print_game_gui(start_game_grid, player_position, player_choice)
    print(game_grid)
else:
    computer_position = np.random.randint(1, 9, size = 1)
    game_grid = print_game_gui(start_game_grid, computer_position, computer_choice)
    print(game_grid)

   
# # GAME STOPS
def found_winner_x(game_grid):
    winner = False
    if game_grid[0][0] == game_grid[0][1] == game_grid[0][2] == 'X':
        winner = True 
    elif game_grid[1][0] == game_grid[1][1] == game_grid[1][2] == 'X':
        winner = True 
    elif game_grid[2][0] == game_grid[2][1] == game_grid[2][2] == 'X':
        winner = True 
    elif game_grid[0][0] == game_grid[1][0] == game_grid[2][0] == 'X':
        winner = True
    elif game_grid[0][1] == game_grid[1][1] == game_grid[2][1] == 'X':
        winner = True
    elif game_grid[0][2] == game_grid[1][2] == game_grid[2][2] == 'X':
        winner = True
    elif game_grid[0][0] == game_grid[1][1] == game_grid[2][2] == 'X':
        winner = True
    elif game_grid[0][2] == game_grid[1][1] == game_grid[2][0] == 'X':
        winner = True
    else:
        winner = False    
    
    return winner

def found_winner_o(game_grid):
    winner = False
    if game_grid[0][0] == game_grid[0][1] == game_grid[0][2] == 'O':
        winner = True 
    elif game_grid[1][0] == game_grid[1][1] == game_grid[1][2] == 'O':
        winner = True 
    elif game_grid[2][0] == game_grid[2][1] == game_grid[2][2] == 'O':
        winner = True 
    elif game_grid[0][0] == game_grid[1][0] == game_grid[2][0] == 'O':
        winner = True
    elif game_grid[0][1] == game_grid[1][1] == game_grid[2][1] == 'O':
        winner = True
    elif game_grid[0][2] == game_grid[1][2] == game_grid[2][2] == 'O':
        winner = True
    elif game_grid[0][0] == game_grid[1][1] == game_grid[2][2] == 'O':
        winner = True
    elif game_grid[0][2] == game_grid[1][1] == game_grid[2][0] == 'O':
        winner = True
    else:
        winner = False    
    
    return winner


def grid_full(game_grid):
    is_full = False 
    counter = 0 
    
    for i in range(3):
        for j in range(3):
            if game_grid[i][j] == ' ':
                counter += 1 
            else:
                counter = counter
    if counter > 0: 
        is_full = False
    else:
        is_full = True 
    
    return is_full 

# is_grid_full = grid_full(game_grid)
# is_someone_winner = found_winner(game_grid)

def game_stop(game_grid):
    is_grid_full = grid_full(game_grid)
    is_x_winner = found_winner_x(game_grid)
    is_o_winner = found_winner_o(game_grid)
    
    stop = False 
    
    if is_grid_full == True:
        stop = True 
    elif is_x_winner == True:
        stop = True 
    elif is_o_winner == True:
        stop = True 
    #elif is_grid_full == False and is_someone_winner == True:
        #stop = True 
    #elif is_grid_full == True and is_someone_winner == False:
        #stop = True 
    else: 
        stop = False 
    
    return stop 
        
should_game_end = game_stop(game_grid)

while should_game_end == False:
    player = decide_player()
    
    if player == computer_choice:
        computer_position = np.random.randint(1, 9, size = 1)
        game_grid = print_game_gui(game_grid, computer_position, computer_choice)
        print("computer played: ", computer_position)
        print(game_grid)
        should_game_end = game_stop(game_grid)
    else:
        player_position = int(input("Which position do you want to play? "))
        game_grid = print_game_gui(game_grid, player_position, player_choice)
        print(game_grid)
        should_game_end = game_stop(game_grid)
    
    
    
if found_winner_x(game_grid) == True:
    print("X WINS!")
elif found_winner_o(game_grid) == True:
    print("O WINS!")
else:
    print("It's a tie...")
    
    


