import os, sys

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

run = True
menu = True
while run:

    print("""
    ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║██║    █████╗  ██║   ███████║██║    █████╗  ██║   ██║   ██║█████╗  
       ██║   ██║██║    ╚════╝  ██║   ██╔══██║██║    ╚════╝  ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
       ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
                                                                        

                                (0)Rules
            
                                (1)Player vs Player
            
                                (2)Player vs Machine
            
                                (3)Machine vs Machine
                                """)
    
    while run:
        x = input("Select the number of your menu: ")
        clearConsole()
        if x == '0':
            print("""
                    ██████╗ ██╗   ██╗██╗     ███████╗███████╗
                    ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
                    ██████╔╝██║   ██║██║     █████╗  ███████╗
                    ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
                    ██║  ██║╚██████╔╝███████╗███████╗███████║
                    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                for Tic-Tac-Toe
                    
            1. The game is played on a grid that's 3 squares by 3 squares.

            2. Player-1(/machine) are X, player-2(/machine) is O. 
            Players take turns putting their marks in empty squares.

            3. The first player to get 3 of their marks 
            in a row (up, down, across, or diagonally) is the winner.

            4. When all 9 squares are full, the game is over.
            If no player has 3 marks in a row, the game ends in a tie.

            """)
                        
            while menu:
                y = input("Type \'Y' for returning to Main Menu: ")
                if y == 'Y' or y == 'y':
                    menu = False
                else:
                    print("Invalid input!")
            clearConsole()
            break
        elif x == '1':
            print("number 1")

        elif x == '2':
            print("number 2")

        elif x == '3':
            print("number 3")
            
        elif x == "Q" or x == 'q':
            run = False

        else:
            print("""
    ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║██║    █████╗  ██║   ███████║██║    █████╗  ██║   ██║   ██║█████╗  
       ██║   ██║██║    ╚════╝  ██║   ██╔══██║██║    ╚════╝  ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
       ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
                                                                        

                                (0)Rules
            
                                (1)Player vs Player
            
                                (2)Player vs Machine
            
                                (3)Machine vs Machine
                                """)
            print("Invalid input!")
