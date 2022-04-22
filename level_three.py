import os, random
from time import sleep
from gameover import win_x, win_o, tie

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
        print('   1   2   3')
        print(' +---+---+---+')
        for y in lista2:
            for s in y:
                print(s + '|', end='')
            print()
            print(' +---+---+---+')


def playerX (lista2): 
    x = random.randrange(0,3)
    y = random.randrange(1,4)
    start = True
    while start:
        #print(x,y)
        if lista2[x][y] == ' . ':
            lista2[x][y] = '\x1b[0;31m X \x1b[0;0m'
            board(lista2)
            print('Automatic mode')
            print('\x1b[0;96mO\x1b[0;0m\'s turn')
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
        if lista2[x][y] == ' . ':
            lista2[x][y] = "\x1b[0;96m O \x1b[0;0m"
            board(lista2)
            print('Automatic mode')
            print('\x1b[0;31mX\x1b[0;0m\'s turn')
            start = False  
        else:
            x = random.randrange(0,3)
            y = random.randrange(1,4)
            pass
        

def wins(list):
    if (list[0][1] == '\x1b[0;31m X \x1b[0;0m' and list[0][2]== '\x1b[0;31m X \x1b[0;0m' and list[0][3]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[1][1] == '\x1b[0;31m X \x1b[0;0m' and list[1][2]== '\x1b[0;31m X \x1b[0;0m' and list[1][3]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[2][1]== '\x1b[0;31m X \x1b[0;0m' and list[2][2]== '\x1b[0;31m X \x1b[0;0m' and list[2][3]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[0][1] == '\x1b[0;31m X \x1b[0;0m'and list[1][2]== '\x1b[0;31m X \x1b[0;0m' and list[2][3]) == '\x1b[0;31m X \x1b[0;0m':    
        #sleep(2) 
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[0][3]== '\x1b[0;31m X \x1b[0;0m' and list[1][2]== '\x1b[0;31m X \x1b[0;0m' and list[2][1]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[0][1]== '\x1b[0;31m X \x1b[0;0m' and list[1][1]== '\x1b[0;31m X \x1b[0;0m' and list[2][1]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[0][2]== '\x1b[0;31m X \x1b[0;0m' and list[1][2]== '\x1b[0;31m X \x1b[0;0m' and list[2][2]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[0][3]== '\x1b[0;31m X \x1b[0;0m' and list[1][3]== '\x1b[0;31m X \x1b[0;0m' and list[2][3]) == '\x1b[0;31m X \x1b[0;0m':
        #sleep(2)
        clearConsole()
        win_x()
        win = True
        return win
    elif (list[0][1]== "\x1b[0;96m O \x1b[0;0m" and list[0][2]== "\x1b[0;96m O \x1b[0;0m" and list[0][3]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[1][1]== "\x1b[0;96m O \x1b[0;0m" and list[1][2]== "\x1b[0;96m O \x1b[0;0m" and list[1][3]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[2][1]== "\x1b[0;96m O \x1b[0;0m" and list[2][2]== "\x1b[0;96m O \x1b[0;0m" and list[2][3]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[0][1]== "\x1b[0;96m O \x1b[0;0m" and list[1][2]== "\x1b[0;96m O \x1b[0;0m" and list[2][3]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[0][3]== "\x1b[0;96m O \x1b[0;0m" and list[1][2]== "\x1b[0;96m O \x1b[0;0m" and list[2][1]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[0][1]== "\x1b[0;96m O \x1b[0;0m" and list[1][1]== "\x1b[0;96m O \x1b[0;0m" and list[2][1]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[0][2]== "\x1b[0;96m O \x1b[0;0m" and list[1][2]== "\x1b[0;96m O \x1b[0;0m" and list[2][2]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    elif (list[0][3]== "\x1b[0;96m O \x1b[0;0m" and list[1][3]== "\x1b[0;96m O \x1b[0;0m" and list[2][3]) == "\x1b[0;96m O \x1b[0;0m":
        sleep(1)
        clearConsole()
        win_o()
        win = True
        return win
    else:
        win = False
        return win

def level_three():
    print('\033[?25l', end="")
    lista2 = [['A',' . ',' . ',' . '],['B',' . ',' . ',' . '],['C',' . ',' . ',' . ']]
    run2 = 1
    board(lista2)
    sleep(1)
    while True:
        lista2 = [['A',' . ',' . ',' . '],['B',' . ',' . ',' . '],['C',' . ',' . ',' . ']]
        while run2:
            clearConsole()
            playerX(lista2)
            run2 += 1
            sleep(2)
            if run2 == 10 and wins(lista2) != True:
                sleep(2)
                clearConsole()
                tie()
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
    print('\033[?25h', end="")
    return False
    


