def obstrange(obst,o_width,res):
    x = obst[0]/res
    y = obst[1]/res
    o_width = o_width/res
    ox= list()           #
    oy= list() 
    # Bottom left corner of the obstacle
    bl = [int(i) for i in [x-o_width/2, y-o_width/2, 0]]

    # Top right corner of the obstacle 
    tr = [int(i) for i in [x+o_width/2, y+o_width/2, 0]]

    for i in range(bl[0],tr[0]):
        for j in range(bl[1],tr[1]):
            ox.append(i)
            oy.append(j)


    return ox,oy 
