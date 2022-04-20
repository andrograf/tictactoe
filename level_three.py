import os, random
from time import sleep

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)






#def new_list():
#    return list([['A',' ',' ',' '],['B',' ',' ',' '],['C',' ',' ',' ']])

#lista = new_list()

def board(lista2):
    for i in range(1):
        print('  1 2 3')
        print(' +-+-+-+')
        for y in lista2:
            for s in y:
                print(s + '|', end='')
            print()
            print(' +-+-+-+')


def playerX (lista2): 
    x = random.randrange(0,3)
    y = random.randrange(1,4)
    start = True
    while start:
        #print(x,y)
        if lista2[x][y] == ' ':
            lista2[x][y] = 'X'
            board(lista2)
            start = False  
        else:
            x = random.randrange(0,3)
            y = random.randrange(1,4)
            pass
    

def playerY (lista2):
    x = random.randrange(0,3)
    y = random.randrange(1,4)
    start = True
    while start:
        #print(x,y)
        if lista2[x][y] == ' ':
            lista2[x][y] = 'O'
            board(lista2)
            start = False  
        else:
            x = random.randrange(0,3)
            y = random.randrange(1,4)
            pass
        

def wins(list):
    if (list[0][1] == 'X' and list[0][2]== 'X' and list[0][3]) == 'X':
        print('a0')
        print('  X WON!')
        win = True
        return win
    elif (list[1][1] == 'X' and list[1][2]== 'X' and list[1][3]) == 'X':
        print('a1')
        print('  X WON!')
        win = True
        return win
    elif (list[2][1]== 'X' and list[2][2]== 'X' and list[2][3]) == 'X':
        print('a2')
        print('  X WON!')
        win = True
        return win
    elif (list[0][1] == 'X'and list[1][2]== 'X' and list[2][3]) == 'X':
        print('a3')
        print('  X WON!')
        win = True
        return win
    elif (list[0][3]== 'X' and list[1][2]== 'X' and list[2][1]) == 'X':
        print('a4')
        print('  X WON!')
        win = True
        return win
    elif (list[0][1]== 'X' and list[1][1]== 'X' and list[2][1]) == 'X':
        print('a5')
        print('  X WON!')
        win = True
        return win
    elif (list[0][2]== 'X' and list[1][2]== 'X' and list[2][2]) == 'X':
        print('a6')
        print('  X WON!')
        win = True
        return win
    elif (list[0][3]== 'X' and list[1][3]== 'X' and list[2][3]) == 'X':
        print('a7')
        print('  X WON!')
        win = True
        return win
    elif (list[0][1]== 'O' and list[0][2]== 'O' and list[0][3]) == 'O':
        print('0')
        print('  O WON!')
        win = True
        return win
    elif (list[1][1]== 'O' and list[1][2]== 'O' and list[1][3]) == 'O':
        print('1')
        print('  O WON!')
        win = True
        return win
    elif (list[2][1]== 'O' and list[2][2]== 'O' and list[2][3]) == 'O':
        print('2')
        print('  O WON!')
        win = True
        return win
    elif (list[0][1]== 'O' and list[1][2]== 'O' and list[2][3]) == 'O':
        print('3')
        print('  O WON!')
        win = True
        return win
    elif (list[0][3]== 'O' and list[1][2]== 'O' and list[2][1]) == 'O':
        print('4')
        print('  O WON!')
        win = True
        return win
    elif (list[0][1]== 'O' and list[1][1]== 'O' and list[2][1]) == 'O':
        print('5')
        print('  O WON!')
        win = True
        return win
    elif (list[0][2]== 'O' and list[1][2]== 'O' and list[2][2]) == 'O':
        print('6')
        print('  O WON!')
        win = True
        return win
    elif (list[0][3]== 'O' and list[1][3]== 'O' and list[2][3]) == 'O':
        print('7')
        print('  O WON!')
        win = True
        return win
    else:
        win = False
        return win

def level_three():
    lista2 = [['A',' ',' ',' '],['B',' ',' ',' '],['C',' ',' ',' ']]
    run2 = 1
    board(lista2)
    sleep(1)
    while True:
        lista2 = [['A',' ',' ',' '],['B',' ',' ',' '],['C',' ',' ',' ']]
        while run2:
            clearConsole()
            playerX(lista2)
            run2 += 1
            sleep(2)
            if run2 == 10 and wins(lista2) != True:
                print('IT\'S A TIE!')
                sleep(2)
                
                break
            elif run2 <=10 and wins(lista2) == True:
                sleep(2)
                
                break
            clearConsole()
            playerY(lista2)
            if run2 <10 and wins(lista2) == True:
                sleep(2)
                
                break
            run2 += 1
            sleep(2)
        run2 = 1
        break
    return False
    


