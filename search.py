import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# creates an instance of HILL_CLIMBER called hc
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

# delete files at the end
os.system("rm *.txt")