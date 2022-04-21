import os
from time import sleep
from level_three import level_three
from level_one_modified import game
from level_two import main
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def main_menu():
    print("""
    ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║██║    █████╗  ██║   ███████║██║    █████╗  ██║   ██║   ██║█████╗  
       ██║   ██║██║    ╚════╝  ██║   ██╔══██║██║    ╚════╝  ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
       ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
                                                                        by \x1b[0;31mTOE\x1b[0;0m \x1b[0;96mFIGHTERS\x1b[0;0m      


                                (0)Rules
            
                                (1)Player vs Player
            
                                (2)Player vs Machine
            
                                (3)Machine vs Machine

                                ('Q')EXIT


                                """)

def rules():
    print("""
                    ██████╗ ██╗   ██╗██╗     ███████╗███████╗
                    ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
                    ██████╔╝██║   ██║██║     █████╗  ███████╗
                    ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
                    ██║  ██║╚██████╔╝███████╗███████╗███████║
                    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                for \x1b[0;31mTic\x1b[0;0m-\x1b[0;96mTac\x1b[0;0m-\x1b[0;31mToe\x1b[0;0m
                    

            1. The game is played on a grid that's 3 squares by 3 squares.


            2. Player-1(/machine) are \x1b[0;31mX\x1b[0;0m, player-2(/machine) is \x1b[0;96mO\x1b[0;0m. 

            Players take turns putting their marks in empty squares.


            3. The first player to get 3 of their marks 

            in a row (up, down, across, or diagonally) is the winner.


            4. When all 9 squares are full, the game is over.
            
            If no player has 3 marks in a row, the game ends in a tie.


            """)

def credits():
    print("""                       
                                \x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m
                                |C|R|E|D|I|T|S|
                                \x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m


                             \x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m
                             |                   |
                             |    Hájas Tamás    |
                             |                   |
                             |  Pusztai Patrícia |
                             |                   |
                             |  Mirejder Róbert  |
                             |                   |
                             \x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m\x1b[0;96m-\x1b[0;0m\x1b[0;31m+\x1b[0;0m""")



run = True

while run:
    clearConsole()
    main_menu()
    while run:
        x = input("Select the number of your menu: ")
        clearConsole()
        if x == '0':
            rules()

            menu = True          
            while menu:
                y = input("Type \'Y' for returning to Main Menu: ")
                if y == 'Y' or y == 'y':
                    clearConsole()
                    menu = False
                elif y == '':
                    clearConsole()
                    rules()
                    pass

                else:
                    clearConsole()
                    rules()
                    print("Invalid input!")
            
            break
        elif x == '1':
            clearConsole()
            game() # level_three.py
            clearConsole()
            break

        elif x == '2':
            clearConsole()
            main() # level_three.py
            clearConsole()
            break

        elif x == '3':
            clearConsole()
            level_three() # level_three.py
            clearConsole()
            break

        elif x == "Q" or x == 'q':
            clearConsole()
            credits()
            sleep(5)
            clearConsole()
            run = False
        
        elif x == '':
            main_menu()
            pass

        else:
            main_menu()
            print("Invalid input!")
