import os, random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def get_empty_board(list):  
    for i in range(len(list)):
        for j in list[i]:
            print(j, end='')
        print()
    
def move_player1(): 
    x = random.randint(0,9)
    y = random.randint(0,9)
    return x, y #meghívni a display boardban???

def display_board(list, x, y):
    move_player1()
    list[x][y]='x'
    for i in range(len(list)):
        for j in list[i]:
            print(j, end='')
        print()

def level_three():
    start = True
    while start:
        get_empty_board(list)
        move_player1()
        display_board(list)
        start = False

        
list = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
#x = int(input("x: " ))
#y = int(input("y: " ))

level_three()

