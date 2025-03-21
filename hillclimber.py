import solution
import constraints
import copy

class HILL_CLIMBER:

    def __init__(self):

        self.parent = solution.SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()

        for currentGeneration in range(constraints.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate()

        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate()
        #print(self.parent.weights)
        #print(self.child.weights)
        #exit()
    
    def Select(self):
        #print(self.parent.fitness)
        #print(self.child.fitness)
        
        if self.parent.fitness < self.child.fitness:
            self.parent = self.child
        
        #exit()

    def Print(self):
        print(self.parent.fitness, self.child.fitness)