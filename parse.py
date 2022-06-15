from utils import *

def parse():
    for i in range(1, end_z-start_z, 2):
        blocks = get_blocks(MC, start_x+1, start_y+1, start_z+i, end_x-1, start_y+1, start_z+i)
        print(len(blocks))

parse()
