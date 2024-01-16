import board



print("Welcome to Tic-Tac")
Player1_Name = input("Enter Player 1 Name : ")
Player1_Choice = input(f"{Player1_Name} , Please Select X (OR) O ")
Player2_Name = input("Enter player 2 Name : ")
Player2_Choice = input(f"{Player2_Name} , Please Select X (OR) O ")

if Player1_Choice.lower() == "x":
    print(f"{Player1_Name} , You have Chosen X")
elif Player1_Choice.lower() == "o":
    print(f"{Player1_Name} , You have Chosen O")

if Player1_Choice.lower() == 'x':
    print(f"{Player2_Name}, You have Chosen O")
elif Player1_Choice.lower() == 'o':
    print(f"{Player2_Name}, You have Chosen X")

print("The game is about to start ..... ")
print("3...2...1...    ")

from time import sleep
from tqdm import tqdm

for i in tqdm(range(10000)):
    sleep(0.0005)


def Row_Column():
    print("Press any number to print your Choice")
    print(f"    {1} |  {2}  | {3} ")
    print("______|_____|_____")
    print("      |     |     ")
    print(f"    {4} |  {5}  | {6} ")
    print("______|_____|_____")
    print("      |     |     ")
    print(f"    {7} |  {8}  | {9} ")

    print("Instructions")
    print("There are 9 boxes each box has number(1-9) ")
    print("Must fill all the boxes")
    print("Player1 will go first")


Row_Column()

print(f"First is your turn {Player1_Name}")


def Row_Column_choice(board, player_choice, box_number):
    row = (box_number - 1) // 3
    col = (box_number - 1) % 3

    # Update the board with the player's choice at the specified box
    board[row][col] = player_choice

    # Display the updated board
    print("   |   |   ")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")


# Initialize an empty 3x3 board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Example: Player 1 (X) makes a move at a specific box (box 8)
player_choice = input(f"Enter your choice {Player1_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))


Row_Column_choice(board, player_choice, box_number)

print(board)

def player2_turn():
    print(f"Next is your turn {Player2_Name}")


player2_turn()

player_choice = input(f"Enter your choice {Player2_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)

def player1_turn():
    print(f"Next is your turn {Player1_Name}")


player1_turn()

player_choice = input(f"Enter your choice {Player1_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)

player2_turn()

player_choice = input(f"Enter your choice {Player2_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)

def player1_turn():
    print(f"Next is your turn {Player1_Name}")


player1_turn()

player_choice = input(f"Enter your choice {Player1_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)


player2_turn()

player_choice = input(f"Enter your choice {Player2_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)

player1_turn()

player_choice = input(f"Enter your choice {Player1_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)

player2_turn()

player_choice = input(f"Enter your choice {Player2_Choice}: ")
box_number = int(input("Enter the box number (1-9): "))

Row_Column_choice(board, player_choice, box_number)

Game_over = False

while not Game_over:
    if (board[0][0] == Player1_Choice and board[0][1] == Player1_Choice and board[0][2] == Player1_Choice) or \
            (board[0][0] == Player2_Choice and board[0][1] == Player2_Choice and board[0][2] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[0][0] == Player1_Choice and board[1][1] == Player1_Choice and board[2][2] == Player1_Choice) or \
            (board[0][0] == Player2_Choice and board[1][1] == Player2_Choice and board[2][2] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[0][2] == Player1_Choice and board[1][1] == Player1_Choice and board[2][0] == Player1_Choice) or \
            (board[0][2] == Player2_Choice and board[1][1] == Player2_Choice and board[2][0] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[1][0] == Player1_Choice and board[1][1] == Player1_Choice and board[1][2] == Player1_Choice) or \
            (board[1][0] == Player2_Choice and board[1][1] == Player2_Choice and board[1][2] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[2][0] == Player1_Choice and board[2][1] == Player1_Choice and board[2][2] == Player1_Choice) or \
            (board[2][0] == Player2_Choice and board[2][1] == Player2_Choice and board[2][2] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[0][0] == Player1_Choice and board[1][0] == Player1_Choice and board[2][0] == Player1_Choice) or \
            (board[0][0] == Player2_Choice and board[1][0] == Player2_Choice and board[2][0] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[0][1] == Player1_Choice and board[1][1] == Player1_Choice and board[2][1] == Player1_Choice) or \
            (board[0][1] == Player2_Choice and board[1][1] == Player2_Choice and board[2][1] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break

    elif (board[0][2] == Player1_Choice and board[1][2] == Player1_Choice and board[2][2] == Player1_Choice) or \
            (board[0][2] == Player2_Choice and board[1][2] == Player2_Choice and board[2][2] == Player2_Choice):
        print(f"{Player1_Name} wins!" if Player1_Choice == 'X' else f"{Player2_Name} wins!")
        Game_over = True
        break
