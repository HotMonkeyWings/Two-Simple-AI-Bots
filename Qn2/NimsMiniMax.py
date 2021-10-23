def minimax(position, maximizingPlayer):
    # Check if final state is attained
    if position[0] == position[1] == 0:
        if maximizingPlayer:
            return 1
        return -1

    # Player 1
    if maximizingPlayer:
        maxEval = -10000
        pileChosen = 1
        # Take from Pile 1
        for pile1 in range(1, position[0] + 1):
            currEval = minimax([position[0] - pile1, position[1]], True)
            maxEval = max(maxEval, currEval)
        
        # Take from Pile 2        
        for pile2 in range(1, position[1] + 1):
            currEval = minimax([position[0], position[1] - pile2], True)
            if maxEval < currEval:
                pileChosen = 2
            maxEval = max(maxEval, currEval)
        
        print("Player 1 Chooses Pile", pileChosen)
        print(position)
        return maxEval
    
    # Player 2
    else:
        minEval = 10000
        pileChosen = 1

        # Take from Pile 1
        for pile1 in range(1, position[0] + 1):
            currEval = minimax([position[0] - pile1, position[1]], True)
            minEval = min(minEval, currEval)
        
        # Take from Pile 2        
        for pile2 in range(1, position[1] + 1):
            currEval = minimax([position[0], position[1] - pile2], True)
            if minEval < currEval:
                pileChosen = 2
            minEval = min(minEval, currEval)
        print("Player 2 Chooses Pile", pileChosen)
        print(position)
        return minEval

print(minimax([3,3], True))