from solution import SOLUTION
import constants as c
import copy
import os
class HILL_CLIMBER:
    # defines a constructor for this class
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        os.system("python simulate.py GUI")
        for currentGeneration in range(c.numberOfGenerations): 
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        # Replaces the parent with its child, if the parent does worse
        if(self.child.fitness < self.parent.fitness):
            self.parent = self.child

    def Print(self):
        print("\n-------------------------------------------------")
        print(self.parent.fitness, " ",self.child.fitness)
        print("-------------------------------------------------")

    def Show_Best(self):
        os.system("python simulate.py GUI")