# The code is only for simulation understanding purposes. All methods are purposely unoptimized to simulate the scenario.
import random

class Environment:
    def __init__(self, environment):
        # Position[0] is for A, Position[1] is for B
        # 0 indicates clean, 1 indicates dirty
        self.locations = environment
    
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
    def __init__(self, startPos, environment, showOutput):
        self.position = startPos
        self.score = 0
        self.environment = Environment(environment)
        self.showOutput = showOutput

    def suck(self):
        print(self.position,"has been sucked. It is now clean.")
        self.environment.locations[self.position] = 0
        self.score += 1
    
    def move(self):
        newPos = random.randint(0,1)

        # Only print output if asked
        if self.showOutput:
            print(("Moved %s" % ("Left" if newPos==0 else "Right")), end='')
            if self.position == newPos:
                print(". But bot was already here.")
            else:
                print()

        self.position = newPos
    
    def runSimulation(self):

        # Print initial details
        print(self.environment)
        print("Start Position: ", self.position)
        
        # Running the simulation for 1000 timesteps.
        moves = 0
        while moves < 1000:
            if self.environment.isDirty(self.position):
                self.suck()
            else:
                self.move()
            moves += 1
        
        print("Performance Score: ", self.score)
        
def main():
    # Iterates through all possible combinations
    for startPosition in range(2):
        for A in range(2):
            for B in range(2):
                Bot = bot(startPosition, [A, B], False)
                Bot.runSimulation()
                print()
    

if __name__ == '__main__':
    main()


