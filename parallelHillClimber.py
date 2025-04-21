import solution
import constraints
import copy
import time
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system('del -f brain*.nndf')
        os.system('del -f fitness*.txt')

        self.matrix_fit = np.zeros((constraints.populationSize, constraints.numberOfGenerations))
        
        self.nextAvailableID = 0
        
        self.parents = {}
        for i in range(constraints.populationSize):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evaluate(self, solutions, generation=None):
        for key, solution in solutions.items():
            solution.Evaluate('DIRECT')
            
            if generation is not None:
                self.matrix_fit[key, generation] = solution.fitness
        
        '''for solution in solutions.values():
            solution.Evaluate('DIRECT')'''

    def Evolve(self):
        self.Evaluate(self.parents, generation = 0)

        for gen in range(1, constraints.numberOfGenerations):
            self.Evolve_For_One_Generation(gen)
            print(f'\rGeneration {gen+1} / {constraints.numberOfGenerations}')
        print()   

        version = os.environ.get('VERSION')

        np.save(f"fitness_matrix_{version}.npy", self.matrix_fit)

    def Evolve_For_One_Generation(self, generation):
        self.children = {}
        for key, parent in self.parents.items():
            child = copy.deepcopy(parent)
            child.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            self.children[key] = child

        self.Mutate()

        self.Evaluate(self.children, generation)

        self.Select()

        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
    
    def Mutate(self):
        for child in self.children.values():
            child.Mutate()
    
    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()
        for key in self.parents:
            parent_fitness = self.parents[key].fitness

            child_fitness = self.children[key].fitness if key in self.children else "N/A"

            print(f"Parent {key}: {parent_fitness} Child {key}: {child_fitness}")
        print()

    def Show_Best(self):
        best = min(self.parents.values(), key=lambda sol: sol.fitness)

        best.Start_Simulation("GUI")