def printGrid(grid):
    for row in range(0,3):
        for col in range(0,3):
            print(grid[row][col], end="" )
        print("")

def main():

    print("hi")

    grid = [['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]

    printGrid(grid)
    counter = 0 
    while counter < 6:
    
        print("\n\n\n\n\n")
        choice = input("where do you want to make your move form 1-9?")
        ok = check_spot(grid,choice, "X")
        printGrid(grid)
        win = win_check(grid, "X")
        if win == True:
            print("X Wins!")
            break

        ################ O goes now!!!! ##############
        print("\n\n\n\n\n")
        choice = input("where do you want to make your move from 1-9")
        ok = check_spot(grid,choice, "O")
        printGrid(grid)
        win = win_check(grid, "O")
        if win == True:
            print("O Wins!")
            break
        counter = counter + 1 


    ####################################
    #play_x = ("make your move")
    #play_0 = ("make your move")
    #x= int(x)
    #0= int(0) 
def check_spot(grid, choice,player):
    code=0
    if choice=="1":
        grid[0][0] = player
    elif choice =="2":
        grid[0][1] = player
    elif choice =="3":
        grid[0][2] = player
    elif choice =="4":
        grid[1][0] = player
    elif choice =="5":
        grid[1][1] = player 
    elif choice =="6":
        grid[1][2] = player 
    elif choice =="7":
        grid[2][0] = player
    elif choice =="8":
        grid[2][1] = player
    elif choice =="9":
        grid[2][2] = player
    
def win_check(grid, player):
    winner = False

    if grid[0][0] == player and grid[0][1] == player and grid[0][2] == player:
        winner = True
    elif grid [1][0] == player and grid[1][1] == player and grid[1][2] == player:
        winner = True 
    elif grid [2][0] == player and grid [2][1] == player and grid [2][2] == player:
        winner = True
    elif grid [0][0] == player and grid [1][0] == player and grid [2][0] == player:
        winner = True
    elif grid [0][1] == player and grid [1][1] == player and grid [2][1] == player:
        winner = True
    elif grid [0][2] == player and grid [1][2] == player and grid [2][2] == player:
        winner = True
    elif grid [0][0] == player and grid [1][1] == player and grid [2][2] == player:
        winner = True 

    return winner

if __name__ == '__main__':
    main()

   