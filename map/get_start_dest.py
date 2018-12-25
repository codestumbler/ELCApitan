import numpy as np
import random 

def get_start_dest(ox,oy, cfg): 
    size_x  = np.ceil( max(ox) - min(ox)) 
    size_y  = np.ceil( max(oy) - min(oy)) 

    # Get initial values 
    x, y    = ox[0], oy[0]

    # drone has to be entirely outside obstacle
    res     = cfg.pm['resolution']
    drone_size_safe = 1/res*(cfg.pm['drone_size'] + cfg.pm['r_safety'])
    ext     = drone_size_safe* np.array([1,1]) 

    # Assure that position is not on an obstacle
    obst    = np.array([ox,oy]).T
    outside = False

    while not outside:  
        z = np.array([x,y])

        for i in range(len(obst)):
            if intersect(z,ext,obst[:][i]): 
                outside = False
                x   = random.randint(0,size_x)
                y   = random.randint(0,size_y) 
            else:
                outside = True 
    return x,y


# -------------------------------------------------------


def intersect(z,ext,target): 
    isonobst = False

    drone = np.array([np.linspace(z[0] - ext[0]/2,z[0] + ext[0]/2),np.linspace(z[1] - ext[1]/2,z[1] + ext[1]/2)]).T

    for i in range(len(drone)): 
        d = abs(target - drone[:][i])
        eps = 0.01
        if np.all(d < np.array([eps, eps])):
            isonobst = True
    return isonobst

