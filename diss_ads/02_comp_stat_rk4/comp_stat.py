import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
import sys
import re

if len(sys.argv)!=5:
    print("Usage: python %s Nsite Nstrip Nsim stat_file" % sys.argv[0])
    sys.exit()

Nsite = int(sys.argv[1])        # number of reactive sites in a strip
Nstrip = int(sys.argv[2])       # number of Strips in simulation
Nsim = int(sys.argv[3])         # number of simulations
outfile = sys.argv[4]           # output file name

 

# read the first data file to figure out the size

[tt,xx] = np.loadtxt('res{}/res1'.format(Nsite),unpack=True,usecols = (0,2))

Npts = len(tt)                  # number of time points

# Initialize 2D array for holding Sim data
xx_sim = np.zeros((Npts, Nsim))

# Read all data files and add values into xx_sum
for i in range(1,Nsim+1):
    xx_sim[:,i-1] = np.loadtxt('res{}/res{}'.format(Nsite, i),unpack=True,usecols = 2)
    
# Calculate percentage of Surface Coverage and Standard Error
surfcov = np.divide(xx_sim, (Nstrip*Nsite))
mean = np.mean(surfcov, axis=1)
stdev = np.std(surfcov, axis=1, ddof=1)
stderr = np.divide(stdev, Nsim)


outfile = outfile + '{}'.format(Nsite)
np.savetxt(outfile, np.transpose([tt, mean, stderr]), fmt=['%.1f', '%.10f', '%.10f'], delimiter='      ', header='Time   Mean    Standard Error')     

sys.exit()