from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

def teleport(x, y, z):
    mc.player.setPos(x, y, z)

def change_blocks(x0, y0, z0, x1, y1, z1, block_type):
    mc.setBlocks(x0, y0, z0, x1, y1, z1, block_type)

def get_blocks(x0, y0, z0, x1, y1, z1):
    return mc.getBlocks(x0, y0, z0, x1, y1, z1, block_type)

block = block.Block(35, 0)
def start():
    change_blocks(400, 0, 600, 400, 10, 620, block)
    change_blocks(400, 0, 600, 420, 0, 620, block)
    change_blocks(400, 0, 600, 420, 10, 600, block)
    change_blocks(420, 0, 600, 420, 10, 620, block)
    change_blocks(400, 0, 620, 420, 10, 620, block)
    change_blocks(420, 0, 600, 420, 10, 620, block)
    teleport(410, 0, 610)

start()

