import numpy as np
def obstrange(obst,o_width,res):
    x = obst[0]/res
    y = obst[1]/res
    o_width = o_width/res
    ox= list()           #
    oy= list() 
    # Bottom left corner of the obstacle
    bl = [float(i) for i in [x-o_width/2, y-o_width/2, 0]]

    # Top right corner of the obstacle 
    tr = [float(i) for i in [x+o_width/2, y+o_width/2, 0]]

    # Make obstacle density twice the resolution 
    for j in np.linspace(bl[0],tr[0], 2/res):
        for k in np.linspace(bl[1],tr[1], 2/res):
            ox.append(j)
            oy.append(k)

    return ox,oy 
