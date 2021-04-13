from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]

simulation = SIMULATION(directOrGui)
simulation.RUN()
simulation.Get_Fitness()
