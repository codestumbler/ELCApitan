import time
import matplotlib.pyplot as plt
import math
from obstrange import *
#from calc_obstacle_map import *

#print(__file__ + " start!!")

def static_map(res, drone_size, r_bubble,show_animation=False): 
    start = time.time()
    # define arena 
    w = 4 
    n_cell = w/res
    ox, oy = [], []

    # define tower
    wt  = 0.4
    wt_bubble = wt + r_bubble

    # borders 
    for i in range(int(n_cell)):
        ox.append(i)
        oy.append(0.0)
    for i in range(int(n_cell)):
        ox.append(n_cell)
        oy.append(i)
    for i in range(int(n_cell)+1):
        ox.append(i)
        oy.append(n_cell)
    for i in range(int(n_cell)+1):
        ox.append(0.0)
        oy.append(i)

    # towers 
    twr1 = [2,2.8,0]
    twr2 = [1.5,1,0]
    twr3 = [3.15,0.7,0]
    twr4 = [3,2,0]

    # Tower 1
    t1_range_x, t1_range_y = obstrange(twr1,wt_bubble,res) 
    # Tower 2
    t2_range_x, t2_range_y = obstrange(twr2,wt_bubble,res) 
    # Tower 3 
    t3_range_x, t3_range_y = obstrange(twr3,wt_bubble,res) 
    # Tower 4 
    t4_range_x, t4_range_y = obstrange(twr4,wt_bubble,res) 
    
    # Complete obstacle arrays
    ox = ox + t1_range_x + t2_range_x + t3_range_x + t4_range_x
    oy = oy + t1_range_y + t2_range_y + t3_range_y + t4_range_y

    end = time.time()
#    print(end-start) 
    if show_animation:
        plt.plot(ox, oy, ".k")
        plt.grid(True)
        plt.axis("equal")
        plt.show()
    return ox,oy, #obmap
