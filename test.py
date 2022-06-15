from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

def teleport(x, y, z):
    mc.player.setPos(x, y, z)

def change_blocks(x0, y0, z0, x1, y1, z1, block_type):
    mc.setBlocks(x0, y0, z0, x1, y1, z1, block_type)
    
def get_blocks(x0, y0, z0, x1, y1, z1):
    return mc.getBlocks(x0, y0, z0, x1, y1, z1, block_type)
    
def start():
    change_blocks(-10, -10, -10, 10, 10, 10, block.AIR)
    teleport(0, 0, 0)

start()

