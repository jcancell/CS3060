import solution
import constraints
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.nextAvailableID = 0
        
        self.parents = {}
        for i in range(0,constraints.populationSize):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        #print(self.parents)
        '''
        self.parent = solution.SOLUTION()
        '''

    def Evolve(self):
        for i in range(len(self.parents)):
            self.parents[i].Evaluate(mode="GUI")
            print(f"Parent {i} Fitness: {self.parents[i].fitness}")
        '''
        self.parent.Evaluate(mode="GUI")

        print("Initial Parent Fitness: " + self.parent.fitness)

        for currentGeneration in range(constraints.numberOfGenerations):
            self.Evolve_For_One_Generation()
        '''
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate()

        self.Print()

        self.Select()

    def Show_Best(self):
        pass
        '''
        self.parent.Evaluate(mode="GUI")
        '''

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
    
    def Mutate(self):
        self.child.Mutate()
    
    def Select(self):
        if self.parent.fitness < self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("\n"+self.parent.fitness, self.child.fitness)