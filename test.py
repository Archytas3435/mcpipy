from mcpi.minecraft import Minecraft
from mcpi import block
from qiskit import QuantumCircuit, Aer, assemble

mc = Minecraft.create()

def teleport(x, y, z):
    mc.player.setPos(x, y, z)

def change_blocks(x0, y0, z0, x1, y1, z1, block_type):
    mc.setBlocks(x0, y0, z0, x1, y1, z1, block_type)

def get_blocks(x0, y0, z0, x1, y1, z1):
    return mc.getBlocks(x0, y0, z0, x1, y1, z1, block_type)

air_block = block.Block(0)
border_block = block.Block(82, 0)
stripe_block = block.Block(82, 14)
start_x, end_x = 400, 420
start_y, end_y = 0, 10
start_z, end_z = 600, 615
def start():
    change_blocks(start_x, start_y, start_z, end_x, end_y, end_z, air_block)
    change_blocks(start_x, start_y, start_z, start_x, end_y, end_z, border_block)
    change_blocks(start_x, start_y, start_z, end_x, start_y, end_z, border_block)
    change_blocks(start_x, start_y, start_z, end_x, end_y, start_z, border_block)
    change_blocks(end_x, start_y, start_z, end_x, end_y, end_z, border_block)
    change_blocks(start_x, start_y, end_z, end_x, end_y, end_z, border_block)
    change_blocks(end_x, start_y, start_z, end_x, end_y, end_z, border_block)
    for i in range(0, end_z-(start_z+1), 2):
        change_blocks(start_x, start_y, start_z+i, end_x, start_y, start_z+i, stripe_block)
    teleport((start_x+end_x)//2, (start_y+end_y)//2, (start_z+end_z)//2)

start()

