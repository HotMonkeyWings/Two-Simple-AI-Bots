# The code is only for simulation understanding purposes. All methods are purposely unoptimized to simulate the scenario.

class Environment:
    def __init__(self, stateA, stateB):
        # Position[0] is for A, Position[1] is for B
        # 0 indicates clean, 1 indicates dirty
        self.locations = [stateA, stateB] 
    
    def isDirty(self, position):
        if self.locations[position] == 0:
            return 0
        else:
            return 1
    
    def __str__(self):
        return "Environment [A:%s, B:%s]"\
            % (("Dirty" if self.locations[0] == 1 else "Clean"),\
               ("Dirty" if self.locations[1] == 1 else "Clean"))

class bot:
    def __init__(self, startPos, environment):
        self.position = startPos
        self.score = 0
        self.environment = environment

    def suck(self):
        self.environment.locations[self.position] = 0
        self.score += 1
    
    def move(self):
        if self.position == 0:
            self.position = 1
        else:
            self.position = 0
    
    def startBot(self):
        # Limiting moves to 2 as beyond that it won't be necessary. The 'moves' variable is hence temporary and not a part of the bot.
        moves = 0
        while moves < 2:
            if self.environment.isDirty(self.position):
                self.suck()
                self.move()
                moves += 1
            else:
                self.score -= 1
                self.move()
                moves += 1
        return self.score
        
def main():
    theEnvironment = Environment(1, 0)
    startPosition = 0

    # Driver code   
    Bot = bot(startPosition, theEnvironment)
    print(theEnvironment)
    print("StartPosition: ", startPosition)
    print("Performance Score: ", Bot.startBot())

if __name__ == '__main__':
    main()


