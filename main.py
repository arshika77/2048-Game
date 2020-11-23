import func as f
import random

def main():

    print("\nWelcome to the 2048 Console world. Let's play!")
    print("Combine given numbers to get a maximum score.\nYou can move numbers to left, right, top or bottom direction.\n")

    # -----------------------------------------Define the features for the game ----------------------------------------------------------------------------

    # This is the basic structure for the 2048 grid. The developer can modify the grid here and the game will run without hiccups

    grid = [['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.']]

    grid, _ = f.addNumber(grid, 'start') #intialize two tiles to 2 or 4

    # Define the grid stack
    gridStack = []
    gridStack.append(grid)
    direction = ['Left', 'Down', 'Right', 'Up', 'X']

    f.printGrid(grid) #Print the inital grid
    loseStatus = 0 #For the curent grid that we have submitted, this variable is not relevant. However, it will be for grids of size 2x2 and 3x3, as it is possible that the agent loses before reaching 8
    f.move.score = 0 # Score of the user

    #---------Make the game runnable by calling relevant functions from the func module and performing relevant operations on them------------------

    while True:

        # The game is being played by an agent

        tmp = random.randint(0, 3) # Generate the move to be played by the agent corresponding to the direction array

        if tmp in range(0, 4):     #Move to the next iteration if tmp not in range - This will continue till the agent provides a valid move

            dir = tmp
            print("\nAction: ", direction[dir])

            if dir == 4:

                print("\nFinal score: " + str(f.move.score))
                break

            else:

                grid = f.move(grid, dir) #Play the move as directed by the agent
                grid, loseStatus = f.addNumber(grid) #Add a random number to the grid before the agent plays the next move
                gridStack.append(grid) #Store the current state
                f.printGrid(grid)

                if loseStatus: # If the agent loses the game (Only in the case of 2x2 or 3x3)
                    print("\nGame Over")
                    print("\nFinal score: " + str(f.move.score))
                    break

                f.move.score = f.sumTiles(grid) #Obtain the score 

                if(f.move.score == 8):

                    print("\nFinal score: " + str(f.move.score))
                    print("\nCongratulations!! You Won")
                    break   # Game ends

                if(f.move.score>8): #Backtrack

                    print("\nCurrent score: " + str(f.move.score))

                    back_count = random.randint(1, 3) #Determine how far to backtrack to

                    print("\nScore is greater than 8. Backtracking ... {} moves".format(min(len(gridStack)-1, back_count)))

                    #-------------------------Backtrack-------------------------------------------
                    grid, gridStack = f.backtrack(gridStack, back_count)
                    f.printGrid(grid)
                    f.move.score = f.sumTiles(grid)
                    if(f.move.score == 8):
                        print("\nFinal score: " + str(f.move.score))
                        print("\nCongratulations!! You Won")
                        break

                print("\nCurrent score: " + str(f.move.score))

    return 0

if __name__ == "__main__":
    main()