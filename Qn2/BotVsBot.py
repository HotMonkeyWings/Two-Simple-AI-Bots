from functools import cache

pathTaken = [
    dict(),             # Player 1
    dict()              # Player 2
]

@cache
def minimax(state, maximizingPlayer=True, showOutput=False):
    # Check if final state is attained
    if state[0] == state[1] == 0:
        if maximizingPlayer:
            return -1
        return 1

    pileChosen = [1, (state[0], state[1]), 0]
    # Player 1
    if maximizingPlayer:
        maxEval = -10000
        # Take from Pile 1
        for pile1 in range(1, state[0] + 1):
            currEval = minimax((state[0] - pile1, state[1]), False, showOutput)
            if maxEval < currEval:
                pileChosen = [1, (state[0] - pile1, state[1]), pile1]
            maxEval = max(maxEval, currEval)
        
        # Take from Pile 2        
        for pile2 in range(1, state[1] + 1):
            currEval = minimax((state[0], state[1] - pile2), False, showOutput)
            if maxEval < currEval:
                pileChosen = [2, (state[0], state[1] - pile2), pile2]
            maxEval = max(maxEval, currEval)
            # (Hey this code was made by Dev Sony, B180297CS)
        if maxEval != -10000:
            if showOutput:
                print("Position was", state)
                print("Player 1 Chooses Pile", pileChosen[0], "and took", str(pileChosen[2]),"stones. Pile states are",pileChosen[1])
                print("MaxEval=", maxEval)
                print()
            pathTaken[0][tuple(state)] = tuple(pileChosen[1])
        return maxEval
    
    # Player 2
    else:
        minEval = 10000

        # Take from Pile 1
        for pile1 in range(1, state[0] + 1):
            currEval = minimax((state[0] - pile1, state[1]), True, showOutput)
            if minEval > currEval:
                pileChosen = [1, (state[0] - pile1, state[1]), pile1]
            minEval = min(minEval, currEval)
        
        # Take from Pile 2        
        for pile2 in range(1, state[1] + 1):
            currEval = minimax((state[0], state[1] - pile2), True, showOutput)
            if minEval > currEval:
                pileChosen = [2, (state[0], state[1] - pile2), pile2]
            minEval = min(minEval, currEval)
        if minEval != 10000:
            if showOutput:
                # (Hey this code was made by Dev Sony, B180297CS)
                print("Position was", state)
                print("Player 2 Chooses Pile", pileChosen[0], "and took", str(pileChosen[2]),"stones. Pile states are",pileChosen[1])
                print("MinEval=", minEval)
                print()
            pathTaken[1][tuple(state)] = tuple(pileChosen[1])
        return minEval


def main():
    # Print possible paths?
    printPossiblePaths = False

    # Adjust the start pile
    startPile = tuple(map(int, input("Enter the number of stones in each pile: ").split()))
    while len(startPile) != 2:
        startPile = tuple(map(int, input("Enter the number of stones in each pile: ").strip().split()))
        print("Only 2 piles are possible!")

    # Driver code
    result = minimax(startPile, True)
    
    if printPossiblePaths:
        print("Player 1's best moves from reachable state:")
        for key in pathTaken[0]:
            print(key, "to", pathTaken[0][key])

        print("\nPlayer 2's best moves from reachable state:")
        for key in pathTaken[1]:
            print(key, "to", pathTaken[1][key])

        print()

    # Setting initial values to traverse through pathsTaken
    startPile = tuple(startPile)
    toggle = 0                                  # Player 1 always starts.
    newPile = pathTaken[toggle][startPile]
    
    while 1:
        print("Player", toggle + 1, ":", startPile, "to", newPile)
        if newPile == (0, 0):
            print("Hence, Player", toggle + 1, "wins!")
            break
        toggle = 0 if toggle == 1 else 1
        startPile, newPile = newPile, pathTaken[toggle][newPile]

if __name__ == "__main__":
    main()