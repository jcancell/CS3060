import os
import hillclimber

'''
for i in range(5):
    os.system("py generate.py")
    os.system("py simulate.py")
'''

hc = hillclimber.HILL_CLIMBER()
hc.Evolve()