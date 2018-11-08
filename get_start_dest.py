import numpy as np
import random 

def get_start_dest(ox,oy): 
    size_x  = max(ox) - min(ox) 
    size_y  = max(oy) - min(oy) 

    # Get initial guess 
    x, y    = ox[0], oy[0]
    z       = np.array([x,y])

    # Assure that position is not on an obstacle
    obst    = np.array([ox,oy])
    obstt   = obst.T
    outside     = False
    while not outside:  
        for i in range(len(obstt)):
            if np.all(z==obstt[:][i]):
                outside = False
                x   = random.randint(0,size_x)
                y   = random.randint(0,size_y) 
            else:
                outside = True 
    return x,y

