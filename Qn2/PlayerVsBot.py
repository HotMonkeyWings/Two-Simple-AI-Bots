pathTaken = [
    dict(),             # Player 1 
    dict()              # Player 2
]

def moveBot(startPile):    
    # Find the new path from pathTaken[] and convert to list.
    newPile = [pathTaken[1][tuple(startPile)][0], pathTaken[1][tuple(startPile)][1]]

    # Print the move to player
    if startPile[0] == newPile[0]:
        print("Bot took", startPile[1] - newPile[1],"stones from Pile 2.")
    if startPile[1] == newPile[1]:
        print("Bot took", startPile[0] - newPile[0],"stones from Pile 1.")
    print("Pile is now", newPile)
    return newPile


def minimax(state, maximizingPlayer=True, showOutput=False):
    # Check if final state is attained
    if state[0] == state[1] == 0:
        if maximizingPlayer:
            return -1
        return 1

    pileChosen = [1,[state[0]], state[1], 0]
    # Player 1
    if maximizingPlayer:
        maxEval = -10000
        # Take from Pile 1
        for pile1 in range(1, state[0] + 1):
            currEval = minimax([state[0] - pile1, state[1]], False, showOutput)
            if maxEval < currEval:
                pileChosen = [1, [state[0] - pile1, state[1]], pile1]
            maxEval = max(maxEval, currEval)
        
        # Take from Pile 2        
        for pile2 in range(1, state[1] + 1):
            currEval = minimax([state[0], state[1] - pile2], False, showOutput)
            if maxEval < currEval:
                pileChosen = [2, [state[0], state[1] - pile2], pile2]
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
            currEval = minimax([state[0] - pile1, state[1]], True, showOutput)
            if minEval > currEval:
                pileChosen = [1, [state[0] - pile1, state[1]], pile1]
            minEval = min(minEval, currEval)
        
        # Take from Pile 2        
        for pile2 in range(1, state[1] + 1):
            currEval = minimax([state[0], state[1] - pile2], True, showOutput)
            if minEval > currEval:
                pileChosen = [2, [state[0], state[1] - pile2], pile2]
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
    # Adjust the start pile
    pileState = list(map(int, input("Enter the number of stones in each pile: ").split()))
    while len(pileState) != 2:
        pileState = list(map(int, input("Enter the number of stones in each pile: ").strip().split()))
        print("Only 2 piles are possible!")

    # Choose the move
    playerStarts = input("Would you like to go first?(Y/N): ")

    if playerStarts == "Y":
        # Driver code
        result = minimax(pileState, True)

        while pileState != [0, 0]:
            print("\n==Player Move==")
            print("Pile is at", pileState)
            pile = int(input("Pile 1 or 2?: ")) - 1
            stones = int(input("Enter number of stones to pick: "))
            pileState[pile] -= stones
            print("Pile is now", pileState)
            if pileState == [0, 0]:
                print("You win!")
                break
            print("\n==Bot's Move==")
            pileState[:] = moveBot(pileState)[:]
        else:
            print("\n==Player Move==\nPile is now at [0, 0]\nBot wins!")
    
    else:
        # Driver code
        result = minimax(pileState, False)

        while pileState != [0, 0]:
            print("\n==Bot's Move==")
            pileState[:] = moveBot(pileState)[:]
            if pileState == [0, 0]:
                print("Bot wins!")
                break

            print("\n==Player's Move==")
            print("Pile is at", pileState)
            pile = int(input("Pile 1 or 2?: ")) - 1
            stones = int(input("Enter number of stones to pick: "))
            pileState[pile] -= stones
            print("Pile is now", pileState)
        else:
            print("You win!")

if __name__ == "__main__":
    main()