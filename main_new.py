#from planner.planner2 import *
from map.get_start_dest import *
from map.static_map import *
from planner.planner2 import a_star_planning 
import config_num_pm as cfg 
import numpy as np 
import pdb 

# debugging
#pdb.set_trace()
# load static map 
ox,oy = static_map(cfg) 

# get start position and destination
Ndrones     = cfg.pm['N_drones']
Ndimensions = cfg.pm['N_dim']
res         = cfg.pm['resolution']

start_dest  = np.empty((0,Ndimensions*2))

for drone in range(Ndrones):
    sx,sy  = get_start_dest(ox,oy,cfg)
    gx,gy  = get_start_dest(ox,oy,cfg)

    sx,sy  = sx*res, sy*res
    gx,gy  = gx*res, gy*res

    # matrix of start and destination of all drones 
    start_dest_drone = np.concatenate(([sx,sy],[gx,gy])) 
    start_dest       = np.vstack((start_dest,start_dest_drone))

# compute trajectories 
drone_size  = cfg.pm['drone_size']
r_bubble    = cfg.pm['r_safety']  
pos         = np.reshape(start_dest[:,0:2], (1,6))
next_pos    = []
opt_trajectories = {}
t = 0

while t < 4: 
    for drone in range(Ndrones):

        # compute dynamic obstacle map
        # give drone physical extension              
        drone_size_safe = drone_size + r_bubble
        drone_pos       = pos[-1,2*drone:2*drone+2]
        range_sox, range_soy  = obstrange(drone_pos, drone_size_safe, res)
        ox.extend(range_sox) 
        oy.extend(range_soy) 
        # plot map with drones current time 
        plt.plot(ox, oy, ".k")
        plt.grid(True)
        plt.axis("equal")


        # optimal path planner 
        # class Node has a problem with numpy floats
        xc =float( drone_pos[0])
        yc =float( drone_pos[1])
        gx =float( start_dest[drone,2])
        gy =float( start_dest[drone,3])
        x_traj, y_traj = a_star_planning(xc,yc,gx,gy,ox,oy,cfg)

        # store all optimal trajectories 
        opt_trajectories[drone] = [x_traj, y_traj]        
        # plot optimal trajectory of current drone 
        plt.plot(x_traj[0], y_traj[0], "-r")
        
    for i in opt_trajectories.keys():
        vals = opt_trajectories[i] 
        next_pos_drone = vals[0] + vals[1]
        next_pos = next_pos + next_pos_drone
    
    print('drone: ' + str(drone)) 
    plt.show()   # update time iterator

    #update position 
    pos = np.vstack((pos,next_pos )) 

    t += 1
# Plot
