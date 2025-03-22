import os
import hillclimber
import parallelHillClimber

#hc = hillclimber.HILL_CLIMBER()
#hc.Evolve()
#hc.Show_Best()

phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()