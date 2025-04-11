import os
import time
import random
import keyboard

# Function to clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game variables
rows, cols = 20, 30  # 20x30 grid
player_pos = [random.randint(1, rows - 2), random.randint(1, cols - 2)]  # Start inside borders
goal = [random.randint(1, rows - 2), random.randint(1, cols - 2)]  # Goal inside borders

clear_screen()  # Initial screen clear

# Game loop
while True:
    # Create 2D game board
    board = [[" " for _ in range(cols)] for _ in range(rows)]

    # Draw borders
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1:  # Top and bottom borders
                board[i][j] = "*"
            elif j == 0 or j == cols - 1:  # Left and right borders
                board[i][j] = "*"

    # Place player and goal (only if not on border)
    board[player_pos[0]][player_pos[1]] = "#"
    board[goal[0]][goal[1]] = "$"

    # Check for win condition
    if player_pos == goal:
        player_pos = [random.randint(1, rows - 2), random.randint(1, cols - 2)]  # New player position
        goal = [random.randint(1, rows - 2), random.randint(1, cols - 2)]  # New goal
        print("Nice job! New game starting...")
        time.sleep(1)
        clear_screen()

    # Print the board
    for row in board:
        print("".join(row))

    # Handle movement with non-blocking input
    if keyboard.is_pressed("w") and player_pos[0] > 1:  # Move up, stop at border
        player_pos[0] -= 1
    elif keyboard.is_pressed("s") and player_pos[0] < rows - 2:  # Move down
        player_pos[0] += 1
    elif keyboard.is_pressed("a") and player_pos[1] > 1:  # Move left
        player_pos[1] -= 1
    elif keyboard.is_pressed("d") and player_pos[1] < cols - 2:  # Move right
        player_pos[1] += 1
    elif keyboard.is_pressed("q"):  # Exit game
        print("Game exited.")
        break

    time.sleep(0.1)  # Control game speed (adjust for responsiveness)
    clear_screen()  # Clear screen for next frame

# Clean up keyboard hooks (optional)
keyboard.unhook_all()
