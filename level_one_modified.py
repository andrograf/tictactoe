import os
from time import sleep
from gameover import game_over
from gameover import win_x, win_o, tie
  
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    
#gameBoard = [["#", "1", "2", "3"], ["A", ".", ".", "."], ["B", ".", ".", "."], ["C", ".", ".", "."]]
rows = 4
cols = 4

def printGameBoard(gameBoard):
    for i in range(1):
        print('   1   2   3')
        print(' +---+---+---+')
        for y in gameBoard:
            for s in y:
                print(s + '|', end='')
            print()
            print(' +---+---+---+')


def winner(gameBoard):
    # X axis

    if gameBoard [0][1] == " X " and gameBoard [0][2] == " X " and gameBoard [0][3] == " X ":
        return win_x()
    
    elif gameBoard [0][1] == " O " and gameBoard [0][2] == " O " and gameBoard [0][3] == " O ":
        return win_o()
    
    elif gameBoard [1][1] == " X " and gameBoard [1][2] == " X " and gameBoard [1][3] == " X ":
        return win_x()
    
    elif gameBoard [1][1] == " O " and gameBoard [1][2] == " O " and gameBoard [1][3] == " O ":
        return win_o()
    
    elif gameBoard [2][1] == " X " and gameBoard [2][2] == " X " and gameBoard [2][3] == " X ":
        return win_x()
    
    elif gameBoard [2][1] == " O " and gameBoard [2][2] == " O " and gameBoard [2][3] == " O ":
        return win_o()
    
    # Y axis
    elif gameBoard [0][1] == " X " and gameBoard [1][1] == " X " and gameBoard [2][1] == " X ":
        return win_x()
    
    elif gameBoard [0][1] == " O " and gameBoard [1][1] == " O " and gameBoard [2][1] == " O ":
        return win_o()
    
    elif gameBoard [0][2] == " X " and gameBoard [1][2] == " X " and gameBoard [2][2] == " X ":
        return win_x()
    
    elif gameBoard [0][2] == " O " and gameBoard [1][2] == " O " and gameBoard [2][2] == " O ":
        return win_o()
    
    elif gameBoard [0][3] == " X " and gameBoard [1][3] == " X " and gameBoard [2][3] == " X ":
        return win_x()
    
    elif gameBoard [0][3] == " O " and gameBoard [1][3] == " O " and gameBoard [2][3] == " O ":
        return win_o()
    
    # Cross
    
    elif gameBoard [0][1] == " X " and gameBoard [1][2] == " X " and gameBoard [2][3] == " X ":
        return win_x()
    
    elif gameBoard [0][1] == " O " and gameBoard [1][2] == " O " and gameBoard [2][3] == " O ":
        return win_o()
    
    elif gameBoard [0][3] == " X " and gameBoard [1][2] == " X " and gameBoard [2][1] == " X ":
        return win_x()
    
    elif gameBoard [0][3] == " O " and gameBoard [1][2] == " O " and gameBoard [2][1] == " O ":
        return win_o()
    
    else:
        return False

def winner1(gameBoard):
    if gameBoard [0][1] == " X " and gameBoard [0][2] == " X " and gameBoard [0][3] == " X ":
        return
    
    elif gameBoard [0][1] == " O " and gameBoard [0][2] == " O " and gameBoard [0][3] == " O ":
        return
    
    elif gameBoard [1][1] == " X " and gameBoard [1][2] == " X " and gameBoard [1][3] == " X ":
        return
    
    elif gameBoard [1][1] == " O " and gameBoard [1][2] == " O " and gameBoard [1][3] == " O ":
        return
    
    elif gameBoard [2][1] == " X " and gameBoard [2][2] == " X " and gameBoard [2][3] == " X ":
        return
    
    elif gameBoard [2][1] == " O " and gameBoard [2][2] == " O " and gameBoard [2][3] == " O ":
        return
    
    # Y axis
    elif gameBoard [0][1] == " X " and gameBoard [1][1] == " X " and gameBoard [2][1] == " X ":
        return
    
    elif gameBoard [0][1] == " O " and gameBoard [1][1] == " O " and gameBoard [2][1] == " O ":
        return
    
    elif gameBoard [0][2] == " X " and gameBoard [1][2] == " X " and gameBoard [2][2] == " X ":
        return

    elif gameBoard [0][2] == " O " and gameBoard [1][2] == " O " and gameBoard [2][2] == " O ":
        return
    
    elif gameBoard [0][3] == " X " and gameBoard [1][3] == " X " and gameBoard [2][3] == " X ":
        return
    
    elif gameBoard [0][3] == " O " and gameBoard [1][3] == " O " and gameBoard [2][3] == " O ":
        return
    
    # Cross
    
    elif gameBoard [0][1] == " X " and gameBoard [1][2] == " X " and gameBoard [2][3] == " X ":
        return
    
    elif gameBoard [0][1] == " O " and gameBoard [1][2] == " O " and gameBoard [2][3] == " O ":
        return
    
    elif gameBoard [0][3] == " X " and gameBoard [1][2] == " X " and gameBoard [2][1] == " X ":
        return
    
    elif gameBoard [0][3] == " O " and gameBoard [1][2] == " O " and gameBoard [2][1] == " O ":
        return
    
    else:
        return False
        

def modify_array(num, turn, gameBoard):
    if num == "A1":
        gameBoard[0][1] = turn
    elif num == "A2":
        gameBoard[0][2] = turn
    elif num == "A3":
        gameBoard[0][3] = turn
    elif num == "B1":
        gameBoard[1][1] = turn
    elif num == "B2":
        gameBoard[1][2] = turn
    elif num == "B3":
        gameBoard[1][3] = turn
    elif num == "C1":
        gameBoard[2][1] = turn
    elif num == "C2":
        gameBoard[2][2] = turn
    elif num == "C3":
        gameBoard[2][3] = turn
        

   
def game():
    turn_counter = 0
    gameBoard = [["A", " . ", " . ", " . "], ["B", " . ", " . ", " . "], ["C", " . ", " . ", " . "]]
    pickable_steps = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "Q"]       
    steps = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"] 
    while True:
        
        if turn_counter % 2 == 1:
            printGameBoard(gameBoard)
            print()
            print("O's turn.")
            numberPicked = input("Choose a step from the coordinates: ").upper()
            clearConsole()
            if numberPicked == "Q":
                game_over()
                sleep(5)
                break
            elif (numberPicked in steps) and numberPicked != 'Q':
                if numberPicked in pickable_steps:
                    pickable_steps.remove(numberPicked)
                    modify_array(numberPicked, " O ", gameBoard)
                    turn_counter += 1
                else:
                    print("Already used input!")
            
            elif (numberPicked not in steps) and numberPicked != 'Q':
                print("Invalid input, try again!")


        
        elif turn_counter % 2 == 0:
            printGameBoard(gameBoard)
            print()
            print("X's turn.")
            numberPicked = input("Choose a step from the coordinates: ").upper()
            clearConsole()
            if numberPicked == "Q":
                game_over()
                sleep(5)
                break
            elif numberPicked in steps:
                if numberPicked in pickable_steps:
                    pickable_steps.remove(numberPicked)
                    modify_array(numberPicked, " X ", gameBoard)
                    turn_counter += 1
                else:
                    print("Already used input!")
            else:
                print("Invalid input, try again!")      
        if winner1(gameBoard) != False:
            printGameBoard(gameBoard)
            sleep(2)
            clearConsole()
            winner(gameBoard)
            sleep(2)
            break
        if is_board_full(gameBoard):
            printGameBoard(gameBoard)
            sleep(1)
            clearConsole()
            tie()
            sleep(3)
            break    

        
def is_board_full(gb):
    for element in gb:
        for e in element:
            if e == " . ":
                return False
    return True
                


#game()

        
