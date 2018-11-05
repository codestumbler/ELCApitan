import random 

def get_start_dest(ox,oy): 
    size_x  = max(ox) - min(ox) 
    size_y  = max(oy) - min(oy) 
    x, y    = ox[0], oy[0]

    while (x in ox and y in oy): 
        x   = random.randint(0,size_x)
        y   = random.randint(0,size_y) 

    return x,y

