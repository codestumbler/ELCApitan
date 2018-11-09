#from planner.planner2 import *
from map.static_map import *
from get_start_dest import *
import config_num_pm as cfg 
import numpy as np 

# load static map 
ox,oy = static_map(cfg) 

# create empty map of same size 
x = range(int(min(ox)),int(max(ox)))
y = range(int(min(oy)),int(max(oy)))

# get start position and destination
Ndrones     = cfg.pm['N_drones']
Ndimensions = cfg.pm['N_dim']
res         = cfg.pm['resolution']

start_dest  = np.empty((0,Ndimensions*2))

for drone in range(Ndrones):
    sx,sy  = get_start_dest(ox,oy) 
    gx,gy  = get_start_dest(ox,oy)
    sx,sy  = sx*res, sy*res
    gx,gy  = gx*res, gy*res

    # matrix of start and destination of all drones 
    start_dest_drone = np.concatenate(([sx,sy],[gx,gy])) 
    start_dest       = np.vstack((start_dest,start_dest_drone))

# compute trajectories 
drone_size  = cfg.pm['drone_size']
r_bubble    = cfg.pm['r_safety']  
pos         = start_dest[:,0:2]

t = 0

while 1: 
    for drone in range(Ndrones):

        # compute dynamic obstacle map
        others = np.delete(pos,drone,0)

        for i in range(len(others)): 
            other = others[i,:]
            # give drone physical extension               
            drone_size_safe = drone_size + r_bubble
            range_sox, range_soy  = obstrange(other, drone_size_safe, res)
            ox.extend(range_sox) 
            oy.extend(range_soy) 

    plt.plot(ox, oy, ".k")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

        # optimal path planner
#        traj = planner2(pos, obstmap)
#        xc,yc = traj[0][0]

        #update position 
        
    # update time iterator
    t += 1
# Plot
