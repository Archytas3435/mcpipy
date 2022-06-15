def parse():
    for i in range(0, end_z-start_z, 2):
        blocks = get_blocks(mc, start_x+1, start_y+1, start_z+i, end_x-1, start_y+1, start_z+i)
        print(blocks)

parse()
