"""board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]

for row_ind in range(len(board)):
    for cell_ind in range (len(board[row_ind])):
        print(board[row_ind][cell_ind], end = "")
    print()
    
x = int(input("Set row: "))
y = int(input("Set col: "))

board[x][y] = "X"

for row_ind in range(len(board)):
    for cell_ind in range (len(board[row_ind])):
        print(board[row_ind][cell_ind], end = "")
    print()

"""
import os
  
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    
gameBoard = [["#", "1", "2", "3"], ["A", ".", ".", "."], ["B", ".", ".", "."], ["C", ".", ".", "."]]
rows = 4
cols = 4

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+---+")


def winner(gameBoard):
    # X axis

    if gameBoard [1][1] == "X" and gameBoard [1][2] == "X" and gameBoard [1][3] == "X":
        return "X has won the game"
    
    elif gameBoard [1][1] == "O" and gameBoard [1][2] == "O" and gameBoard [1][3] == "O":
        return "O has won the game"
    
    elif gameBoard [2][1] == "X" and gameBoard [2][2] == "X" and gameBoard [2][3] == "X":
        return "X has won the game"
    
    elif gameBoard [2][1] == "O" and gameBoard [2][2] == "O" and gameBoard [2][3] == "O":
        return "O has won the game"
    
    elif gameBoard [3][1] == "X" and gameBoard [3][2] == "X" and gameBoard [3][3] == "X":
        return "X has won the game"
    
    elif gameBoard [3][1] == "O" and gameBoard [3][2] == "O" and gameBoard [3][3] == "O":
        return "O has won the game"
    
    # Y axis
    elif gameBoard [1][1] == "X" and gameBoard [2][1] == "X" and gameBoard [3][1] == "X":
        return "X has won the game"
    
    elif gameBoard [1][1] == "O" and gameBoard [2][1] == "O" and gameBoard [3][1] == "O":
        return "O has won the game"
    
    elif gameBoard [1][2] == "X" and gameBoard [2][2] == "X" and gameBoard [3][2] == "X":
        return "X has won the game"
    
    elif gameBoard [1][2] == "O" and gameBoard [2][2] == "O" and gameBoard [3][2] == "O":
        return "O has won the game"
    
    elif gameBoard [1][3] == "X" and gameBoard [2][3] == "X" and gameBoard [3][3] == "X":
        return "X has won the game"
    
    elif gameBoard [1][3] == "O" and gameBoard [2][3] == "O" and gameBoard [3][3] == "O":
        return "O has won the game"
    
    # Cross
    
    elif gameBoard [1][1] == "X" and gameBoard [2][2] == "X" and gameBoard [3][3] == "X":
        return "X has won the game"
    
    elif gameBoard [1][1] == "O" and gameBoard [2][2] == "O" and gameBoard [3][3] == "O":
        return "O has won the game"
    
    elif gameBoard [1][3] == "X" and gameBoard [2][2] == "X" and gameBoard [3][1] == "X":
        return "X has won the game"
    
    elif gameBoard [1][3] == "O" and gameBoard [2][2] == "O" and gameBoard [3][1] == "O":
        return "O has won the game"
    
    else:
        return False


    
        

def modify_array(num, turn):
    if num == "A1":
        gameBoard[1][1] = turn
    elif num == "A2":
        gameBoard[1][2] = turn
    elif num == "A3":
        gameBoard[1][3] = turn
    elif num == "B1":
        gameBoard[2][1] = turn
    elif num == "B2":
        gameBoard[2][2] = turn
    elif num == "B3":
        gameBoard[2][3] = turn
    elif num == "C1":
        gameBoard[3][1] = turn
    elif num == "C2":
        gameBoard[3][2] = turn
    elif num == "C3":
        gameBoard[3][3] = turn
        
pickable_steps = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]       

steps = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"] 
   
def game():
    turn_counter = 0
    while True:
        if turn_counter % 2 == 1:
            printGameBoard()
            print()
            print("O's turn.")
            numberPicked = input("Choose a step from the coordinates: ").upper()
            clearConsole()
            if numberPicked in steps:
                if numberPicked in pickable_steps:
                    pickable_steps.remove(numberPicked)
                    modify_array(numberPicked, "O")
                    turn_counter += 1
                else:
                    print("Already used input!")
            else:
                print("Invalid input, try again!")


        
        elif turn_counter % 2 == 0:
            printGameBoard()
            print()
            print("X's turn.")
            numberPicked = input("Choose a step from the coordinates: ").upper()
            clearConsole()
            if numberPicked in steps:
                if numberPicked in pickable_steps:
                    pickable_steps.remove(numberPicked)
                    modify_array(numberPicked, "X")
                    turn_counter += 1
                else:
                    print("Already used input!")
            else:
                print("Invalid input, try again!")      
        if winner(gameBoard) != False:
            printGameBoard()
            print()
            print(winner(gameBoard))
            break
        if is_board_full(gameBoard):
            printGameBoard()
            print()
            print("It's a tie!")
            break
        
def is_board_full(gb):
    for element in gb:
        for e in element:
            if e == ".":
                return False
    return True
                


game()

        
