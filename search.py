import os
import hillclimber
import parallelHillClimber
import sys
import numpy as np

#hc = hillclimber.HILL_CLIMBER()
#hc.Evolve()
#hc.Show_Best()

if len(sys.argv) != 2 or sys.argv[1] not in ['A', 'B', 'C', 'D']:
    print("Usage: python search.py A|B|C|D")
    exit(1)

experiment = sys.argv[1]
os.environ['VERSION'] = experiment  # Pass it as an environment variable


phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
'''
data = np.load('fitness_matrix_A.npy')
print("Matrix A")
print(data)

data = np.load('fitness_matrix_B.npy')
print("Matrix B")
print(data)
'''