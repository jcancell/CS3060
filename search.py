import os
import hillclimber
import parallelHillClimber
import sys

#hc = hillclimber.HILL_CLIMBER()
#hc.Evolve()
#hc.Show_Best()

if len(sys.argv) != 2 or sys.argv[1] not in ['A', 'B']:
    print("Usage: python search.py A|B")
    exit(1)

experiment = sys.argv[1]
os.environ['EXPERIMENT_VERSION'] = experiment  # Pass it as an environment variable


phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()