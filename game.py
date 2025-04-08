import os
import time
import random
from keyboard  # Import from your keystroke module

# Function to clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game variables
rows, cols = 20, 30  # 10x20 grid
player_pos = list([random.randint(0,10), random.randint(0,10)])  # Start at row 5, column 10
goal = list([random.randint(0,23), random.randint(0,23)])

clear_screen()  # Clear screen for smooth movement
# Game loop
while True:
    key = keyboard.read_key() # Read key input

    # Move the player
    if key == 'w' and player_pos[0] > 0:    # Move up
        player_pos[0] -= 1
    elif key == 's' and player_pos[0] < rows - 1:  # Move down
        player_pos[0] += 1
    elif key == 'a' and player_pos[1] > 0:    # Move left
        player_pos[1] -= 1
    elif key == 'd' and player_pos[1] < cols - 1:  # Move right
        player_pos[1] += 1

    # Create 2D game board
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    board[player_pos[0]][player_pos[1]] = "#"  # Place the player
    board[goal[0]][goal[1]] = "$"

    if player_pos == goal:
        player_pos = [0,0]
        goal = list([random.randint(0,19), random.randint(0,19)])
        print("Nice job, New game!")
        time.sleep(1)
        clear_screen()  # Clear screen for smooth movement
    
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1:  # Top and Bottom borders
                board[i][j] = "*"
            elif j == 0 or j == cols - 1:  # Left and Right borders
                board[i][j] = "*"
    
    # Print the board
    for row in board:
        print("".join(row))

    time.sleep(0.1)  # Control speed
