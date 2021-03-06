import numpy as np
import random
def AntColony(nants, evap, bpp, seed):
#nants = # of ants, evap = evaporation rate, bpp =bin packing problem pick(1 or 2), seed = random number seed
#nbins = # of bins, phmatrix = pheromone matrix, binweight = weight of bin list, itemweight = weight of item list
    random.seed(seed)
    if (bpp == 1): 
        nbins = 10
#number of items = 500, sets item weight to its position in the list of items
        itemweight = [i + 1 for i in range(500)] 
    elif (bpp == 2):
        nbins = 50
#sets item weight to position squared 
        itemweight=[((i + 1) * (i +1 )) for i in range(500)] 
# Distribute pheromone on the matrix randomly 
    phmatrix=[[random.random() for j in range(nbins)] for i in range(500)] 	
#repeat step 2 to 5, number of iterations had to be reduced due to computing power.	
    for iter in range(250): 
        stoe = [[] for n in range(nants)] #set of S to E paths
        div=np.sum(phmatrix, axis = 1) 
        prob=[phmatrix[i]/div[i] for i in range(500)]
        for n in range(nants):
            for i in range(500):
#appends nbins random steps from S to E
                stoe[n].append(np.random.choice([j for j in range(nbins)], p=prob[i])+1)
# fitness (best-worst path)
        fit = [0 for n in range(nants)] 
        for n in range(nants):
            binweight=[0 for j in range(nbins)]
            for i in range(500):
                binweight[stoe[n][i]-1] = binweight[stoe[n][i]-1] + itemweight[stoe[n][i]-1]
            fit[n] = max(binweight) - min(binweight)
        for i in range(500):
#updates pheromone with best path for 100/fitness
            phmatrix[i][stoe[fit.index(min(fit))][i]-1] += 100/min(fit)
# evaporate the pheromone
        phmatrix = [[evap * phmatrix[i][j] for j in range(nbins)] for i in range(500)] 

# best and worst fitness of first and last iteration 
        if (iter == 0):
            print("First iteration best: ", min(fit))
        elif (iter == 249):
            print("Last iteration best: ", min(fit))
    
    return 0

AntColony(10, 0.5, 2, 5)