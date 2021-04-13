from solution import SOLUTION
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    # defines a constructor for this class
    def __init__(self):
        # delete files befor beginning
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm tmp*.txt")
        self.nextAvailableID = 0
        self.parents = dict()
        for i in range(c.populationSize):   #range(x) is exclusive
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Evolve(self):
        # Evaluate each of the parents
        self.Evaluate(self.parents)
        # Evolving every generation
        for currentGeneration in range(c.numberOfGenerations): 
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print("\n ")
        self.Print()
        print(" ")
        self.Select()

    def Spawn(self):
        self.children = dict()
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        # Replaces the parent with its child, if the parent does worse
        for key in self.parents:
            if(self.children[key].fitness < self.parents[key].fitness):
                self.parents[key] = self.children[key]

    def Print(self):
        for key in self.parents:
            # print("\n-------")
            # print(" ")
            print("parent: ", self.parents[key].fitness)
            print("child: ", self.children[key].fitness)
            
    def Show_Best(self):
        # initialize minFitness to the 1st instance
        minFitness = self.parents[0].fitness
        keyOfBest = 0
        for key in self.parents:
            if (self.parents[key].fitness < minFitness):
                minFitness = self.parents[key].fitness
                keyOfBest = key
    
        self.parents[keyOfBest].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
        
             
