from re import I
import os
import time
from gameover import game_over




def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def insertLetter(letter, pos, board):
    board[pos] = letter


def spaceIsFree(pos, board):
    return board[pos] == ' '


def printBoard(board):
    board2 = []
    for i in board:
        if i == " ":
            board2.append(".")
        else:
            board2.append(i)
        
    print("   1   2   3")
    print(' +---+---+---+')
    print('A| ' + board2[1] + ' | ' + board2[2] + ' | ' + board2[3] + ' |')
    print(' +---+---+---+')
    print('B| ' + board2[4] + ' | ' + board2[5] + ' | ' + board2[6] + ' |')
    print(' +---+---+---+')
    print('C| ' + board2[7] + ' | ' + board2[8] + ' | ' + board2[9] + ' |')
    print(' +---+---+---+')


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le))

def kill_move():
    stop = False
    return stop


def playerMove(board, keyCorrect):
    run = True
    while run:

        move = input('Please select a position to place X: ')
        try:
            move = keyCorrect[move.lower()]
            move = abs(int(move))
            if move == 0:
                clearConsole()
                game_over()
                return True

            elif 1 <= move < 10:
                if spaceIsFree(move,board):
                    #run = False
                    insertLetter('X', move, board)
                    break
                else:
                    clearConsole()
                    printBoard(board)
                    print('Sorry, this space is occupied. Please try an other one!')
            elif move > 10:
                clearConsole()
                printBoard(board)
                print('Please type a coordinate within the range')
            
        except:
            clearConsole()
            printBoard(board)
            print("Please type a valid coordinate!")


def compMove(board):
    possibleMoves = [x for x, letter in enumerate(board)
                     if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            # nem módosítja az egész boardot, hanem másolja
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    time.sleep(1)

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    clearConsole()
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    board = [' ' for x in range(10)]
    keyCorrect = {"a1":1, "a2":2, "a3":3,"b1":4, "b2":5, "b3":6,"c1":7, "c2":8, "c3":9, 'q':0}
    printBoard(board)
    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove(board, keyCorrect)
            if playerMove == True:
                time.sleep(5)
                clearConsole()
                break
            else:
                printBoard(board)
                clearConsole()
            
        else:
            #printBoard(board)
            time.sleep(1.5)
            clearConsole()
            game_over()
            time.sleep(5)
            break

        if not (isWinner(board, 'X')):
            move = compMove(board)
            if move == 0:
                clearConsole()
                pass
                #print('Tie game!')
            else:
                printBoard(board)
                time.sleep(1.5)
                clearConsole()
                insertLetter('O', move, board)
                # print('Computer placed an O in position', move, ':')
                printBoard(board)
        else:
            printBoard(board)
            print("You won the game!")
            time.sleep(3)
            break
    if isBoardFull(board):
        printBoard(board)
        print('Tie game!')
        time.sleep(3)


#main()  # ezt ki kell majd szedni

# board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]



