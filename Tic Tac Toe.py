print("Welcome to Tic-Tac")
Player1_Name = input("Enter Player 1 Name : ")
Player1_Choice = input(f"{Player1_Name} , Please Select X (OR) O ")
Player2_Name = input("Enter player 2 Name : ")
Player2_choice = input(f"{Player2_Name} , Please Select X (OR) O ")

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

def Column():
    print("Press any number to print your Choice")
    print     (f"    {1} |  {2}  | {3} ")
    print     ("______|_____|_____")
    print     ("      |     |     ")
    print     (f"    {4} |  {5}  | {6} ")
    print     ("______|_____|_____")
    print     ("      |     |     ")
    print     (f"    {7} |  {8}  | {9} ")

    print("Instructions")
    print("There are 9 boxes each box has number(1-9) ")
    print("Must fill all the boxes")
    print("Player1 will go first")

Column()






