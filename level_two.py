from re import I
import os
import time


board = [' ' for x in range(10)]
keyCorrect = {"a1":1, "a2":2, "a3":3,"b1":4, "b2":5, "b3":6,"c1":7, "c2":8, "c3":9}

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
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



def playerMove():
    run = True
    while run:

        move = input('Please select a position to place X: ')
        try:
            move = keyCorrect[move.lower()]
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied. Please try an other one!')
            else:
                print('Please type a coordinate within the range')
        except:
            print("Please type a valid coordinate!")


def compMove():
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
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
            clearConsole()
        else:
            print("Sorry, the computer won this time!")
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                clearConsole()
                pass
                #print('Tie game!')
            else:
                insertLetter('O', move)
                # print('Computer placed an O in position', move, ':')
                printBoard(board)
        else:
            printBoard(board)
            print("You won the game!")
            break
    if isBoardFull(board):
        printBoard(board)
        print('Tie game!')


main()  # ezt ki kell majd szedni

# board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]



