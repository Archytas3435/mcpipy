from mcpi import block
from mcpi.minecraft import Minecraft

MC = Minecraft.create()

def teleport(mc, x, y, z):
    mc.player.setPos(x, y, z)

def change_blocks(mc, x0, y0, z0, x1, y1, z1, block_type):
    mc.setBlocks(x0, y0, z0, x1, y1, z1, block_type)

def get_blocks(mc, x0, y0, z0, x1, y1, z1):
    return list(mc.getBlocks(x0, y0, z0, x1, y1, z1))

air_block = block.Block(0)
border_block = block.Block(35, 0)
stripe_block = block.Block(35, 14)
hadamard_block = block.Block(13)
not_block = block.Block(14)
cnot_start_block = block.Block(15)
cnot_end_block = block.Block(16)
measure_block = block.Block(22)
qubit_0_block = block.Block(5)
qubit_25_block = block.Block(7)
qubit_50_block = block.Block(12)
qubit_75_block = block.Block(41)
qubit_100_block = block.Block(49)
start_x, end_x = 400, 420
start_y, end_y = 0, 10
start_z, end_z = 600, 616
